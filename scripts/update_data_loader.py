import os
import json
from collections import defaultdict

def retrieve_supported_events():
    directory = os.path.dirname(os.path.abspath(__file__)) + '/../jsonschema'
    dataLoaderStructure = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') and file != "catalog.json":
                with open(root + "/" + file, "r") as eventFile:
                    product = root.split("/")[-2]
                    data = json.load(eventFile)
                    if product not in dataLoaderStructure:
                        dataLoaderStructure[product] = {
                            "eventTypes": [],
                            "metricTypes": [],
                        }
                    dataLoaderStructure[product]["eventTypes"].extend(data["cloudeventTypes"])
                    if "metricTypes" in data:
                        dataLoaderStructure[product]["metricTypes"].extend(data["metricTypes"])
                    dataLoaderStructure[product]["eventTypes"] = sorted(set(dataLoaderStructure[product]["eventTypes"]))
                    dataLoaderStructure[product]["metricTypes"] = sorted(set(dataLoaderStructure[product]["metricTypes"]))

    return dict(sorted(dataLoaderStructure.items()))

def writeSupportedEventsToDataLoaderFile(supportedEvents):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../DataLoader.json", "w") as eventsFile:
        eventsFile.write(json.dumps(supportedEvents, indent=4))
        eventsFile.write("\n")


if __name__ == "__main__":
    supportedEvents = retrieve_supported_events()
    writeSupportedEventsToDataLoaderFile(supportedEvents)
