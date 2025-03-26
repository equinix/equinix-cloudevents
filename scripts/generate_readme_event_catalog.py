import os
import json
import script_constants as sc
import re

def dropdowns(type, supported):

    released_events = [e for e in supported if e.get("isReleased")]
    preview_events = [e for e in supported if e.get("inPreview")]
    dropdowns = "#### " + type

    if preview_events:
        dropdowns += "\n\n<details>\n<summary>In Preview</summary>\n\n"
        dropdowns += "<table>\n\t<tr>\n\t\t<th>Name</th>\n\t\t<th>Description</th>\n\t</tr>\n"
        dropdowns += "\n".join(f"\t<tr>\n\t\t<td>{e["name"]}</td>\n\t\t<td>{e["description"]}</td>\n\t</tr>" for e in preview_events)
        dropdowns += "\n</table>"
        dropdowns += "\n\n</details>\n\n"
    if released_events:
        dropdowns += "\n\n<details>\n<summary>Released</summary>\n\n"
        dropdowns += "<table>\n\t<tr>\n\t\t<th>Name</th>\n\t\t<th>Description</th>\n\t</tr>\n"
        dropdowns += "\n".join(f"\t<tr>\n\t\t<td>{e["name"]}</td>\n\t\t<td>{e["description"]}</td>\n\t</tr>" for e in released_events)
        dropdowns += "\n</table>"
        dropdowns += "\n\n</details>\n"""
    return dropdowns if len(dropdowns) > 20 else ""

def schema_entry(schema):
    cloudEventTypes = ""
    metrics = ""
    alerts = ""
    sla_categories = set()

    if sc.EVENTS in schema:
        cloudEventTypes = dropdowns(sc.README_EVENTS, schema[sc.EVENTS])
    if sc.METRICS in schema:
        metrics = dropdowns(sc.README_METRICS, schema[sc.METRICS])
    if sc.ALERTS in schema:
        alerts = dropdowns(sc.README_ALERTS, schema[sc.ALERTS])
    
    for key in [sc.EVENTS, sc.METRICS, sc.ALERTS]:
        if key in schema:
            for item in schema[key]:
                if "slaCategoryCode" in item:
                    print(f"found slaCategory: {item["slaCategoryCode"]}")
                    sla_categories.add(item["slaCategoryCode"])
    sla_info = ""
    if sla_categories:
        sla_links = [f"[{category}](#{category.lower().replace(' ', '-')})" for category in sorted(sla_categories, key=str.lower) if category.strip()]
        sla_info = "#### SLA Categories\n" + "<br>\n".join(sla_links)
        print(f"sla info : {sla_info}")
    return f"""---
### {schema["domain"]}
#### DataSchema [JSON]({schema["url"]})
#### Data Type
`{schema["datatype"]}`
{sla_info} 
#### Supported Events, Metrics, and Alerts
{cloudEventTypes}
{metrics}
{alerts}"""

def load_sla_details(sla_filepath):
    with open(sla_filepath, "r") as sla_file:
        return json.load(sla_file)

def sla_table(sla_data):
    table = "<table>\n<tr>\n"
    
    # Extract headers from the first entry
    headers = ["Category", "Code", "Collection Interval", "Reporting", "Streaming Latency", "Query Latency", "Retention PT5M", "Retention PT1H", "Retention PT1D"]
    table += "".join(f"<th>{header}</th>" for header in headers) + "</tr>\n"

    all_sla_entries = sorted(
        sla_data.get("metricsSLA", []) + sla_data.get("eventsSLA", []),
        key=lambda item: (item.get("code", "") or "").strip().lower()
    )
    # Extract values for metrics SLA
    for item in all_sla_entries:
        category_id = item.get("code", "").lower().replace(" ", "-")
        table += f"<tr id='{category_id}'>\n"
        table += f"<td>{item.get('category', '')}</td>"
        table += f"<td>{item.get('code', '')}</td>"
        table += f"<td>{item.get('collectionInterval', '')}</td>"
        table += f"<td>{item.get('reporting', '')}</td>"
        table += f"<td>{item.get('streamingLatency', '')}</td>"
        table += f"<td>{item.get('queryLatency', '')}</td>"
        table += f"<td>{item.get('retentionPT5M', '')}</td>"
        table += f"<td>{item.get('retentionPT1H', '')}</td>"
        table += f"<td>{item.get('retentionPT1D', '')}</td>"
        table += "</tr>\n"

    table += "</table>\n"
    return table
    
def replace_readme_catalog():
    readme_path = os.path.dirname(os.path.abspath(__file__)) + "/../README.md"
    catalog_path = os.path.dirname(os.path.abspath(__file__)) + "/../jsonschema/catalog.json"
    slaCategory_path = os.path.dirname(os.path.abspath(__file__)) + "/../jsonschema/slaCategories.json"
   
    with open(catalog_path, "r") as catalog_file:
        catalog = json.load(catalog_file)
        schemas = "\n".join(map(schema_entry, catalog["schemas"]))

    with open(slaCategory_path, "r") as sla_file:
        sla_data = json.load(sla_file)
        sla_table_content = sla_table(sla_data)
    
    with open(readme_path, "r+") as readme_file:
        content = readme_file.read()
        readme_file.seek(0)
        
        sla_start = "<!-- SLA_CATEGORY -->"
        sla_end = "<!-- SLA_CATEGORY_END -->"
        sla_pattern = rf"{sla_start}.*?{sla_end}"
        
        if re.search(sla_pattern, content, flags=re.DOTALL):
                updated_content = re.sub(sla_pattern, f"{sla_start}\n{sla_table_content}\n{sla_end}",
                content,
                flags=re.DOTALL 
            )
        else:
            updated_content = content + f"\n\n{sla_start}\n{sla_table_content}\n{sla_end}\n"
        
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
