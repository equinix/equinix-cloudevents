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
                            sc.EVENTS:  [],
                            sc.METRICS: [],
                            sc.ALERTS:  []
                        }
                    
                    for event in data.get(sc.EVENTS, []):
                        if isinstance(event, dict) and "name" in event and "releaseStatus" in event:
                            dataLoaderStructure[domain][sc.EVENTS].append({
                                "name": event["name"],
                                "releaseStatus": event["releaseStatus"]
                            })
                            

                    for metric in data.get(sc.METRICS, []):
                        if isinstance(metric, dict) and "name" in metric and "releaseStatus" in metric:
                            dataLoaderStructure[domain][sc.METRICS].append({
                                "name": metric["name"],
                                "releaseStatus": metric["releaseStatus"]
                            })
                            
                    for alert in data.get(sc.ALERTS, []):
                        if isinstance(alert, dict) and "name" in alert and "releaseStatus" in alert:
                            dataLoaderStructure[domain][sc.ALERTS].append({
                                "name": alert["name"],
                                "releaseStatus": alert["releaseStatus"]
                            })
                            
                    for section in [sc.EVENTS, sc.METRICS, sc.ALERTS]:
                        dataLoaderStructure[domain][section] = sorted(
                            dataLoaderStructure[domain][section], 
                            key=lambda x: (x["releaseStatus"] != "released", x["name"])
                        )

    dataLoaderStructure = dict(sorted(dataLoaderStructure.items()))

    return dataLoaderStructure

def writeSupportedEventsToDataLoaderFile(supportedEvents):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../DataLoader.json", "w") as eventsFile:
        eventsFile.write(json.dumps(supportedEvents, indent=4))
        eventsFile.write("\n")


if __name__ == "__main__":
    main()
