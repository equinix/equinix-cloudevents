import os
import json
import script_constants as sc
import re

# Schemas whose name ends with one of these are grouped into per-domain tables
# with a Product column. Anything else keeps its own per-file section.
GROUPED_SUFFIXES = ["Event", "ChangeEvent", "Alert", "Metric"]

def get_colored_text(text):
    font_color = 'black'
    if 'PURPLE' in text:
        font_color = 'purple'
    elif 'BROWN' in text:
        font_color = 'brown'
    elif 'BLUE' in text:
        font_color = 'blue'
    return f"<span style='color:{font_color}'>{text}</span>"

def slo_cell(entry):
    code = entry.get('sloCategoryCode')
    if not code:
        return '-'
    anchor = code.lower().replace(' ', '-')
    return f"<a href='#{anchor}'> {get_colored_text(code)}</a>"

def slugify(heading):
    """GitHub heading anchor: lowercase, punctuation dropped, spaces to hyphens."""
    return re.sub(r"[^\w\- ]", "", heading).strip().lower().replace(" ", "-")

def collapsible(summary, count, body):
    """Fold a table behind a <details> so long domains stay scannable."""
    return (f"<details>\n<summary><b>{summary}</b> ({count})</summary>\n\n"
            f"{body}\n</details>\n")

def table_of_contents(headings):
    lines = "\n".join(f"- [{h}](#{slugify(h)})" for h in headings)
    return f"### Contents\n\n{lines}\n"

def createTable(type, supported):
    if not supported:
        return ""

    list = "<table>\n\t<tr>\n\t\t<th>Name</th>\n\t\t<th>Description</th>\n\t\t<th>Release Status</th>\n\t\t<th>SLO Category</th>\n\t</tr>\n"

    list += "\n".join(
        f"\t<tr>\n\t\t<td>{x['name']}</td>\n\t\t<td>{x['description']}</td>\n\t\t<td>{x.get('releaseStatus') if x.get('releaseStatus') else '-'}</td>\n"
        f"\t<td>{slo_cell(x)}</td>\n"
        f"\t</tr>"
        for x in supported
    )

    list += "\n</table>\n"
    return collapsible(type, len(supported), list)

def schema_entry(schema):
    cloudEventTypes = ""
    metrics = ""
    alerts = ""

    if sc.EVENTS in schema:
        cloudEventTypes = createTable(sc.README[sc.EVENTS], schema[sc.EVENTS])
    if sc.METRICS in schema:
        metrics = createTable(sc.README[sc.METRICS], schema[sc.METRICS])
    if sc.ALERTS in schema:
        alerts = createTable(sc.README[sc.ALERTS], schema[sc.ALERTS])

    return f"""---
### {schema["domain"]}
#### DataSchema [JSON]({schema["url"]})
#### Data Type
`{schema["datatype"]}`
#### Supported Events, Metrics, and Alerts
{cloudEventTypes}
{metrics}
{alerts}"""

def is_grouped(schema):
    return any(schema["name"].endswith(s) for s in GROUPED_SUFFIXES)

def domain_group(schema):
    """fabric -> Equinix Fabric, network_edge -> Equinix Network Edge"""
    segment = schema["url"].split("/jsonschema/equinix/")[1].split("/")[0]
    return "Equinix " + " ".join(w.capitalize() for w in segment.split("_"))

def product_label(name):
    """ConnectionChangeEvent -> Connection, DeviceInterfaceMetricAlert -> Device Interface"""
    base = name
    # longest first, so ChangeEvent wins over Event and leaves the product intact
    for suffix in sorted(GROUPED_SUFFIXES, key=len, reverse=True):
        if base.endswith(suffix):
            base = base[: -len(suffix)]
            break
    # MetricAlert/MetricEvent leave a trailing "Metric" that is not the product
    if base.endswith("Metric") and base != "Metric":
        base = base[: -len("Metric")]
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", base) or name

def product_for(schema):
    """Product label, keeping any qualifier the per-file heading used to show."""
    label = product_label(schema["name"])
    qualifier = re.search(r"\(([^)]+)\)\s*$", schema["domain"])
    return f"{label} ({qualifier.group(1)})" if qualifier else label

def schema_index_table(schemas):
    rows = "\n".join(
        f"\t<tr>\n\t\t<td>{product_for(s)}</td>\n"
        f"\t\t<td><a href='{s['url']}'>JSON</a></td>\n"
        f"\t\t<td><code>{s['datatype']}</code></td>\n\t</tr>"
        for s in sorted(schemas, key=lambda s: (product_for(s), s["datatype"]))
    )
    table = ("<table>\n\t<tr>\n\t\t<th>Product</th>\n\t\t<th>DataSchema</th>\n"
             "\t\t<th>Data Type</th>\n\t</tr>\n" + rows + "\n</table>\n")
    return collapsible("Schemas", len(schemas), table)

def grouped_table(type, rows):
    """rows: list of (product, entry) across every schema in the domain"""
    if not rows:
        return ""

    if type == sc.README[sc.METRICS]:
        table = ("<table>\n\t<tr>\n\t\t<th>Product</th>\n\t\t<th>Metric Names</th>\n\t\t<th>Description</th>\n"
                 "\t\t<th>Release Status</th>\n\t\t<th>SLO Category</th>\n\t</tr>\n")
    else:
        table = ("<table>\n\t<tr>\n\t\t<th>Product</th>\n\t\t<th>Cloud Event Types</th>\n\t\t<th>Description</th>\n"
                 "\t\t<th>Release Status</th>\n\t\t<th>SLO Category</th>\n\t</tr>\n")
    table += "\n".join(
        f"\t<tr>\n\t\t<td>{product}</td>\n\t\t<td>{x['name']}</td>\n\t\t<td>{x['description']}</td>\n"
        f"\t\t<td>{x.get('releaseStatus') if x.get('releaseStatus') else '-'}</td>\n"
        f"\t\t<td>{slo_cell(x)}</td>\n\t</tr>"
        for product, x in sorted(rows, key=lambda r: (r[0], r[1]["name"]))
    )
    table += "\n</table>\n"
    return collapsible(type, len(rows), table)

def grouped_entry(group, schemas):
    tables = ""
    for key in [sc.EVENTS, sc.ALERTS, sc.METRICS]:
        rows = [(product_for(s), x) for s in schemas for x in s.get(key, [])]
        tables += grouped_table(sc.README[key], rows) + "\n"

    return f"""---
### {group}
{schema_index_table(schemas)}
{tables}"""

def build_catalog(schemas):
    """Group Evnet/ChangeEvent/Alert/Metric schemas by domain."""
    groups = {}
    for s in schemas:
        groups.setdefault(domain_group(s), []).append(s)

    sections = []
    for group in sorted(groups):
        members = groups[group]
        grouped = [s for s in members if is_grouped(s)]
        if grouped:
            sections.append((group, grouped_entry(group, grouped)))
        # anything not matching the three categories keeps its own section
        sections += [(s["domain"], schema_entry(s))
                     for s in sorted(members, key=lambda s: s["url"])
                     if not is_grouped(s)]

    toc = table_of_contents([heading for heading, _ in sections])
    return "\n".join([toc] + [body for _, body in sections])

def slo_table(slo_data):
    table = "<table>\n<tr>\n"

    # Extract headers from the first entry
    headers = ['Category Code', 'Reporting Interval', 'Reporting Latency Max', 'Stream Latency Max', 'Original Data Retention', 'Hourly Aggregation Retention', 'Daily Aggregation Retention']
    table += "".join(f"<th>{header}</th>" for header in headers) + "</tr>\n"

    all_slo_entries = sorted(
        slo_data.get('metricsSLO', []) + slo_data.get('eventsSLO', []) + slo_data.get('alertsSLO', []),
        key=lambda item: (item.get('code', '') or '').lower()
    )
    # Extract values for metrics SLO
    for item in all_slo_entries:
        category_id = item.get('category_code', '').lower().replace(' ', '-')
        table += f"<tr id='{category_id}'>\n"
        table += f"<td>{get_colored_text(item.get('category_code'))}</td>"
        table += f"<td>{item.get('reportingInterval', '-') or '-'}</td>"
        table += f"<td>{item.get('reportingLatencyMax', '-')or '-'}</td>"
        table += f"<td>{item.get('streamLatencyMax', '-')or '-'}</td>"
        table += f"<td>{item.get('orignalDataRetention', '-') or '-'}</td>"
        table += f"<td>{item.get('1HAggregationRetention', '-') or '-'}</td>"
        table += f"<td>{item.get('1DAggregationRetention', '-') or '-'}</td>"
        table += "</tr>\n"

    table += "</table>\n"
    return table

def replace_readme_catalog():
    readme_path = os.path.dirname(os.path.abspath(__file__)) + "/../README.md"
    catalog_path = os.path.dirname(os.path.abspath(__file__)) + "/../jsonschema/catalog.json"
    sloCategory_path = os.path.dirname(os.path.abspath(__file__)) + "/../jsonschema/sloCategories.json"

    with open(catalog_path, "r") as catalog_file:
        catalog = json.load(catalog_file)
        schemas = build_catalog(catalog["schemas"])

    with open(sloCategory_path, "r") as slo_file:
        slo_data = json.load(slo_file)
        slo_table_content = slo_table(slo_data)

    with open(readme_path, "r+") as readme_file:
        content = readme_file.read()
        readme_file.seek(0)
        updated_content = content

        slo_start = "<!-- SLO_CATEGORY -->"
        slo_end = "<!-- SLO_CATEGORY_END -->"
        slo_pattern = rf"{slo_start}.*?{slo_end}"

        if re.search(slo_pattern, content, flags=re.DOTALL):
                updated_content = re.sub(slo_pattern, f"{slo_start}\n{slo_table_content}\n{slo_end}",
                content,
                flags=re.DOTALL
            )

        generation_start = "<!-- CATALOG_GENERATION_START -->"
        generation_end = "<!-- CATALOG_GENERATION_END -->"
        catalog_pattern = rf"{generation_start}.*?{generation_end}"

        if re.search(catalog_pattern, updated_content, flags=re.DOTALL):
                updated_content = re.sub(catalog_pattern, f"{generation_start}\n{schemas}\n{generation_end}",
                updated_content,
                flags=re.DOTALL
            )

        readme_file.write(updated_content)
        readme_file.truncate()


if __name__ == "__main__":
    replace_readme_catalog()
