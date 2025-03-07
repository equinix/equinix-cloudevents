import os
import json
import script_constants as sc

def dropdowns(type, supported):
    dropdowns = "#### " + type
    if len(supported[sc.PREVIEW]) > 0:
        dropdowns += "\n\n<details>\n<summary>In Preview</summary>\n\n"
        dropdowns += "<table>\n\t<tr>\n\t\t<th>Name</th>\n\t\t<th>Description</th>\n\t</tr>\n"
        dropdowns += "\n".join(map(lambda x: f"\t<tr>\n\t\t<td>{x["name"]}</td>\n\t\t<td>{x["description"]}</td>\n\t</tr>", supported[sc.PREVIEW]))
        dropdowns += "\n</table>"
        dropdowns += "\n\n</details>\n\n"
    if len(supported[sc.RELEASED]) > 0:
        dropdowns += "\n\n<details>\n<summary>Released</summary>\n\n"
        dropdowns += "<table>\n\t<tr>\n\t\t<th>Name</th>\n\t\t<th>Description</th>\n\t</tr>\n"
        dropdowns += "\n".join(map(lambda x: f"\t<tr>\n\t\t<td>{x["name"]}</td>\n\t\t<td>{x["description"]}</td>\n\t</tr>", supported[sc.RELEASED]))
        dropdowns += "\n</table>"
        dropdowns += "\n\n</details>\n"""
    return dropdowns if len(dropdowns) > 20 else ""

def schema_entry(schema):
    cloudEventTypes = ""
    metrics = ""
    alerts = ""
    if sc.EVENTS in schema:
        cloudEventTypes = dropdowns(sc.README_EVENTS, schema[sc.EVENTS])
    if sc.METRICS in schema:
        metrics = dropdowns(sc.README_METRICS, schema[sc.METRICS])
    if sc.ALERTS in schema:
        alerts = dropdowns(sc.README_ALERTS, schema[sc.ALERTS])
    return f"""---
### {schema["domain"]}
#### DataSchema [JSON]({schema["url"]})
#### Data Type
`{schema["datatype"]}`
#### Supported Events, Metrics, and Alerts
{cloudEventTypes}
{metrics}
{alerts}"""

def replace_readme_catalog():
    readme_path = os.path.dirname(os.path.abspath(__file__)) + "/../README.md"
    catalog_path = os.path.dirname(os.path.abspath(__file__)) + "/../jsonschema/catalog.json"
    with open(catalog_path, "r") as catalog_file:
        catalog = json.load(catalog_file)
        schemas = "\n".join(map(schema_entry, catalog["schemas"]))

    with open(readme_path, "r+") as readme_file:
        content = readme_file.read()
        readme_file.seek(0)
        generation_start = "<!-- CATALOG_GENERATION_START -->"
        generation_end = "<!-- CATALOG_GENERATION_END -->"
        header = content[:content.index(generation_start)+len(generation_start)]
        footer = content[content.index(generation_end):]
        readme_file.write(f"""{header}
{schemas}
{footer}""")
        readme_file.truncate()


if __name__ == "__main__":
    replace_readme_catalog()
