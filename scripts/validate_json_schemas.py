import os
from jsonschema import validate
import json

def validateJsonSchemas():
    validationSchemaFile = os.path.dirname(os.path.abspath(__file__))+"/jsonschema-org-schema.json"
    with open(validationSchemaFile, "r") as schemaFile:
        schema = json.load(schemaFile)
    directory = os.path.dirname(os.path.abspath(__file__)) + '/../jsonschema'
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') and os.path.basename(root) != "jsonschema":
                with open(root + "/" + file, "r") as eventFile:
                    data = json.load(eventFile)
                    validate(instance=data, schema=schema)


if __name__ == "__main__":
    validateJsonSchemas()
