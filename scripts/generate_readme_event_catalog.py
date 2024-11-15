import os
import json

def table_row(schema):
    cloudEventTypes = "<br>\n".join(map(lambda x: f"`{x}`", schema["cloudeventTypes"]))
    metrics = ""
    if "metricNames" in schema:
        metricNames = "<br>\n".join(map(lambda x: f"`{x}`", schema["metricNames"]))
        metrics = f"#### Metric Type(s)\n{metricNames}"
    return f"""### {schema["domain"]}
#### DataSchema [JSON]({schema["url"]})
#### Data Type
`{schema["datatype"]}`
#### CloudEvent Type(s)
{cloudEventTypes}
{metrics}"""

def replace_readme_catalog():
    readme_path = os.path.dirname(os.path.abspath(__file__)) + "/../README.md"
    catalog_path = os.path.dirname(os.path.abspath(__file__)) + "/../jsonschema/catalog.json"
    with open(catalog_path, "r") as catalog_file:
        catalog = json.load(catalog_file)
        schemas = "\n".join(map(table_row, catalog["schemas"]))

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