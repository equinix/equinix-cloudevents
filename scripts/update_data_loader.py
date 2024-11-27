import os
import json
from collections import defaultdict


# Constant declarations
RELEASED = "released"
PREVIEW = "preview"

EVENTS = "cloudeventTypes"
METRICS = "metricNames"
ALERTS = "alertNames"




def retrieve_supported_events():
    directory = os.path.dirname(os.path.abspath(__file__)) + '/../jsonschema'
    dataLoaderStructure = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') and file != "catalog.json":
                with open(root + "/" + file, "r") as eventFile:
                    domain = root.split("/")[-2]
                    data = json.load(eventFile)
                    if domain not in dataLoaderStructure:
                        dataLoaderStructure[domain] = {
                            EVENTS: {
                                RELEASED: [],
                                PREVIEW: []
                            },
                            METRICS: {
                                RELEASED: [],
                                PREVIEW: []
                            },
                            ALERTS: {
                                RELEASED: [],
                                PREVIEW: []
                            }
                        }
                    data[EVENTS][RELEASED]
                    dataLoaderStructure[domain][EVENTS][RELEASED].extend(data[EVENTS][RELEASED])
                    dataLoaderStructure[domain][EVENTS][PREVIEW].extend(data[EVENTS][PREVIEW])
                    dataLoaderStructure[domain][METRICS][RELEASED].extend(data[METRICS][RELEASED])
                    dataLoaderStructure[domain][METRICS][PREVIEW].extend(data[METRICS][PREVIEW])
                    dataLoaderStructure[domain][ALERTS][RELEASED].extend(data[ALERTS][RELEASED])
                    dataLoaderStructure[domain][ALERTS][PREVIEW].extend(data[ALERTS][PREVIEW])

                    dataLoaderStructure[domain][EVENTS][RELEASED] = sorted(set(dataLoaderStructure[domain][EVENTS][RELEASED]))
                    dataLoaderStructure[domain][EVENTS][PREVIEW] = sorted(set(dataLoaderStructure[domain][EVENTS][PREVIEW]))
                    dataLoaderStructure[domain][METRICS][RELEASED] = sorted(set(dataLoaderStructure[domain][METRICS][RELEASED]))
                    dataLoaderStructure[domain][METRICS][PREVIEW] = sorted(set(dataLoaderStructure[domain][METRICS][PREVIEW]))
                    dataLoaderStructure[domain][ALERTS][RELEASED] = sorted(set(dataLoaderStructure[domain][ALERTS][RELEASED]))
                    dataLoaderStructure[domain][ALERTS][PREVIEW] = sorted(set(dataLoaderStructure[domain][ALERTS][PREVIEW]))

    dataLoaderStructure = dict(sorted(dataLoaderStructure.items()))

    return dataLoaderStructure

def writeSupportedEventsToDataLoaderFile(supportedEvents):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../DataLoader.json", "w") as eventsFile:
        eventsFile.write(json.dumps(supportedEvents, indent=4))
        eventsFile.write("\n")


if __name__ == "__main__":
    supportedEvents = retrieve_supported_events()
    writeSupportedEventsToDataLoaderFile(supportedEvents)
