import os
from jsonschema import validate
import json
import script_constants as sc

def validateJsonSchemas():
    validationSchemaFile = os.path.dirname(os.path.abspath(__file__))+"/jsonschema-org-schema.json"
    with open(validationSchemaFile, "r") as schemaFile:
        schema = json.load(schemaFile)
    directory = os.path.dirname(os.path.abspath(__file__)) + '/../jsonschema'
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') and sc.VERSION_DIR.match(os.path.basename(root)):
                with open(root + "/" + file, "r") as eventFile:
                    data = json.load(eventFile)
                    validate(instance=data, schema=schema)


if __name__ == "__main__":
    validateJsonSchemas()
