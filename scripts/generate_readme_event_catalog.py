import os
import json

def table_row(schema):
    cloudEventTypes = "<br>".join(map(lambda x: f"`{x}`", schema["cloudeventTypes"]))
    metrics = ""
    if "metricNames" in schema:
        metricNames = "<br>".join(map(lambda x: f"`{x}`", schema["metricNames"]))
        metrics = f"<br>Metric Type(s):<br>{metricNames}"
    return f"|{schema["product"]}|[JSON]({schema["url"]})|<br>Data Type:<br>`{schema["datatype"]}`<br>CloudEvent Type(s):<br>{cloudEventTypes}<br>{metrics}|"

def replace_readme_catalog():
    readme_path = os.path.dirname(os.path.abspath(__file__)) + "/../README.md"
    catalog_path = os.path.dirname(os.path.abspath(__file__)) + "/../jsonschema/catalog.json"
    with open(catalog_path, "r") as catalog_file:
        catalog = json.load(catalog_file)
        schemas = "\n".join(map(table_row, catalog["schemas"]))

    replacement_readme_catalog = f"""|Product|Schemas|Types|

{schemas}"""
    
    with open(readme_path, "r+") as readme_file:
        content = readme_file.read()
        readme_file.seek(0)
        generation_start = "<!-- CATALOG_GENERATION_START -->"
        generation_end = "<!-- CATALOG_GENERATION_END -->"
        header = content[:content.index(generation_start)+len(generation_start)]
        footer = content[content.index(generation_end):]
        readme_file.write(f"""{header}
{replacement_readme_catalog}
{footer}""")
        readme_file.truncate()


if __name__ == "__main__":
    replace_readme_catalog()