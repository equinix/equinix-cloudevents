import os
import json
import script_constants as sc
import re

def createTable(type, supported):
    if not supported:
        return ""

    list = f"#### {type}\n\n"
    list += "<table>\n\t<tr>\n\t\t<th>Name</th>\n\t\t<th>Description</th>\n\t\t<th>Release Status</th>\n\t\t<th>SLO Category</th>\n\t</tr>\n"

    list += "\n".join(
        f"\t<tr>\n\t\t<td>{x['name']}</td>\n\t\t<td>{x['description']}</td>\n\t\t<td>{'Released' if x.get('isReleased') else 'In Preview'}</td>\n"
        f"\t<td>{f'<a href=\'#{x.get('sloCategoryCode', '').lower().replace(' ', '-')}\'> {x.get('sloCategoryCode')}</a>' if x.get('sloCategoryCode') else '-'}</td>\n"
        f"\t</tr>"
        for x in supported
    )

    list += "\n</table>\n"
    return list if len(list) > 20 else ""

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

def slo_table(slo_data):
    table = "<table>\n<tr>\n"
    
    # Extract headers from the first entry
    headers = ['Category', 'Code', 'Reporting Interval', 'Reporting Latency Max', 'Streaming Latency Max', 'Query Latency Max', 'Original Data Retention', '1 Hour Aggregation Retention', '1 Day Aggregation Retention']
    table += "".join(f"<th>{header}</th>" for header in headers) + "</tr>\n"

    all_slo_entries = sorted(
        slo_data.get('metricsSLO', []) + slo_data.get('eventsSLO', []),
        key=lambda item: (item.get('code', '') or '').lower()
    )
    # Extract values for metrics SLO
    for item in all_slo_entries:
        category_id = item.get('code', '').lower().replace(' ', '-')
        table += f"<tr id='{category_id}'>\n"
        table += f"<td>{item.get('category', '-')or '-'}</td>"
        table += f"<td>{item.get('code', '-') or '-'}</td>"
        table += f"<td>{item.get('reportingInterval', '-') or '-'}</td>"
        table += f"<td>{item.get('reportingLatencyMax', '-')or '-'}</td>"
        table += f"<td>{item.get('streamingLatencyMax', '-')or '-'}</td>"
        table += f"<td>{item.get('queryLatencyMax', '-')or '-'}</td>"
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
        schemas = "\n".join(map(schema_entry, catalog["schemas"]))

    with open(sloCategory_path, "r") as slo_file:
        slo_data = json.load(slo_file)
        slo_table_content = slo_table(slo_data)
    
    with open(readme_path, "r+") as readme_file:
        content = readme_file.read()
        readme_file.seek(0)
        
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
