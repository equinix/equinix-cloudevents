import os
import json
from collections import defaultdict


# Constant declarations
DEV = "dev"
PROD = "prod"

CLOUD_EVENTS = "cloudeventTypes"

EVENTS = "eventTypes"
METRICS = "metricNames"
ALERTS = "alertNames"


def retrieve_supported_events():
    directory = os.path.dirname(os.path.abspath(__file__)) + '/../jsonschema'
    dataLoaderStructure = {
        DEV: {},
        PROD: {}
    }
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') and file != "catalog.json":
                with open(root + "/" + file, "r") as eventFile:
                    domain = root.split("/")[-2]
                    data = json.load(eventFile)
                    if domain not in dataLoaderStructure[DEV]:
                        dataLoaderStructure[DEV][domain] = {
                            EVENTS: [],
                            METRICS: [],
                            ALERTS: [],
                        }

                    dataLoaderStructure[DEV][domain][EVENTS].extend(data[CLOUD_EVENTS])
                    dataLoaderStructure[DEV][domain][METRICS].extend(data[METRICS])
                    dataLoaderStructure[DEV][domain][ALERTS].extend(data[ALERTS])

                    dataLoaderStructure[DEV][domain][EVENTS] = sorted(set(dataLoaderStructure[DEV][domain][EVENTS]))
                    dataLoaderStructure[DEV][domain][METRICS] = sorted(set(dataLoaderStructure[DEV][domain][METRICS]))
                    dataLoaderStructure[DEV][domain][ALERTS] = sorted(set(dataLoaderStructure[DEV][domain][ALERTS]))
                    
                    if data["prodEnabled"]:
                        if domain not in dataLoaderStructure[PROD]:
                            dataLoaderStructure[PROD][domain] = {
                                EVENTS: [],
                                METRICS: [],
                                ALERTS: [],
                            }
                        for event, prodEnabled in data[CLOUD_EVENTS].items():
                            if prodEnabled:
                                dataLoaderStructure[PROD][domain][EVENTS].append(event)
                        for metric, prodEnabled in data[METRICS].items():
                            if prodEnabled:
                                dataLoaderStructure[PROD][domain][METRICS].append(metric)
                        
                        for alert, prodEnabled in data[ALERTS].items():
                            if prodEnabled:
                                dataLoaderStructure[PROD][domain][ALERTS].append(alert)
                        
                        dataLoaderStructure[PROD][domain][EVENTS] = sorted(set(dataLoaderStructure[PROD][domain][EVENTS]))
                        dataLoaderStructure[PROD][domain][METRICS] = sorted(set(dataLoaderStructure[PROD][domain][METRICS]))
                        dataLoaderStructure[PROD][domain][ALERTS] = sorted(set(dataLoaderStructure[PROD][domain][ALERTS]))

    dataLoaderStructure[DEV] = dict(sorted(dataLoaderStructure[DEV].items()))
    dataLoaderStructure[PROD] = dict(sorted(dataLoaderStructure[PROD].items()))

    return dataLoaderStructure

def writeSupportedEventsToDataLoaderFile(supportedEvents):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../DataLoader_DEV.json", "w") as eventsFile:
        eventsFile.write(json.dumps(supportedEvents[DEV], indent=4))
        eventsFile.write("\n")
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../DataLoader_PROD.json", "w") as eventsFile:
        eventsFile.write(json.dumps(supportedEvents[PROD], indent=4))
        eventsFile.write("\n")


if __name__ == "__main__":
    supportedEvents = retrieve_supported_events()
    writeSupportedEventsToDataLoaderFile(supportedEvents)
