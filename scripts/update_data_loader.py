import os
import json
import script_constants as sc

def main():
    supportedEvents = retrieve_supported_events()
    writeSupportedEventsToDataLoaderFile(supportedEvents)

def retrieve_supported_events():
    directory = os.path.dirname(os.path.abspath(__file__)) + '/../jsonschema'
    dataLoaderStructure = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') and os.path.basename(root) != "jsonschema":
                with open(root + "/" + file, "r") as eventFile:
                    domain = root.split("/")[-2]
                    data = json.load(eventFile)
                    if domain not in dataLoaderStructure:
                        dataLoaderStructure[domain] = {
                            sc.EVENTS: {
                                sc.RELEASED: [],
                                sc.PREVIEW: []
                            },
                            sc.METRICS: {
                                sc.RELEASED: [],
                                sc.PREVIEW: []
                            },
                            sc.ALERTS: {
                                sc.RELEASED: [],
                                sc.PREVIEW: []
                            }
                        }
                    
                    for event in data.get(sc.EVENTS, []):
                        if isinstance(event, dict):
                            status = event.get("releaseStatus")
                            if status == "released":
                                dataLoaderStructure[domain][sc.EVENTS][sc.RELEASED].append(event["name"])
                            elif status == "preview":
                                dataLoaderStructure[domain][sc.EVENTS][sc.PREVIEW].append(event["name"])

                    for metric in data.get(sc.METRICS, []):
                        if isinstance(metric, dict):
                            status = metric.get("releaseStatus")
                            if status ==  "released":
                                dataLoaderStructure[domain][sc.METRICS][sc.RELEASED].append(metric["name"])
                            elif status == "preview":
                                dataLoaderStructure[domain][sc.METRICS][sc.PREVIEW].append(metric["name"])

                    for alert in data.get(sc.ALERTS, []):
                        if isinstance(alert, dict):
                            status = alert.get("releaseStatus")
                            if status == "released":
                                dataLoaderStructure[domain][sc.ALERTS][sc.RELEASED].append(alert["name"])
                            elif status == "preview":
                                dataLoaderStructure[domain][sc.ALERTS][sc.PREVIEW].append(alert["name"])
                    
                    dataLoaderStructure[domain][sc.EVENTS][sc.RELEASED] = sorted(set(dataLoaderStructure[domain][sc.EVENTS][sc.RELEASED]))
                    dataLoaderStructure[domain][sc.EVENTS][sc.PREVIEW] = sorted(set(dataLoaderStructure[domain][sc.EVENTS][sc.PREVIEW]))
                    dataLoaderStructure[domain][sc.METRICS][sc.RELEASED] = sorted(set(dataLoaderStructure[domain][sc.METRICS][sc.RELEASED]))
                    dataLoaderStructure[domain][sc.METRICS][sc.PREVIEW] = sorted(set(dataLoaderStructure[domain][sc.METRICS][sc.PREVIEW]))
                    dataLoaderStructure[domain][sc.ALERTS][sc.RELEASED] = sorted(set(dataLoaderStructure[domain][sc.ALERTS][sc.RELEASED]))
                    dataLoaderStructure[domain][sc.ALERTS][sc.PREVIEW] = sorted(set(dataLoaderStructure[domain][sc.ALERTS][sc.PREVIEW]))

    dataLoaderStructure = dict(sorted(dataLoaderStructure.items()))

    return dataLoaderStructure

def writeSupportedEventsToDataLoaderFile(supportedEvents):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../DataLoader.json", "w") as eventsFile:
        eventsFile.write(json.dumps(supportedEvents, indent=4))
        eventsFile.write("\n")


if __name__ == "__main__":
    main()
