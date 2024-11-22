import os
import json

def retrieve_json_schemas():
    directory = os.path.dirname(os.path.abspath(__file__)) + '/../jsonschema'
    json_schemas = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') and file != "catalog.json":
                with open(root + "/" + file, "r") as eventFile:
                    data = json.load(eventFile)
                    # if data["prodEnabled"]:
                    #     events = sorted([event for event, prodEnabled in data["cloudeventTypes"].items() if prodEnabled])
                    #     metrics = sorted([event for event, prodEnabled in data["metricNames"].items() if prodEnabled])
                    #     alerts = sorted([event for event, prodEnabled in data["alertNames"].items() if prodEnabled])
                    events = sorted(data["cloudeventTypes"].keys())
                    metrics = sorted(data["metricNames"].keys())
                    alerts = sorted(data["alertNames"].keys())
                    newItem = {
                        "url": data["$id"],
                        "domain": data["domain"],
                        "name": data["name"],
                        "description": data["definitions"]["Data"]["description"],
                        "datatype": data["datatype"],
                        "cloudeventTypes": events,
                        "metricNames": metrics,
                        "alertNames": alerts
                    }
                    json_schemas.append(newItem)
    json_schemas.sort(key=lambda x: x["url"])
    return json_schemas

def write_json_schemas_to_catalog_file(json_schemas):
    catalog = {
        "$schema": 'https://json.schemastore.org/schema-catalog',
        "version": 1,
        "schemas": json_schemas
    }
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../jsonschema/catalog.json", "w") as catalogFile:
        catalogFile.write(json.dumps(catalog, indent=4))
        catalogFile.write("\n")


if __name__ == "__main__":
    json_schemas = retrieve_json_schemas()
    write_json_schemas_to_catalog_file(json_schemas)