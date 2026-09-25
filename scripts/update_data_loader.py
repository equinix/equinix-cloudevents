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
        # equinix/<domain>/<version>[/<product>]; schemas may sit directly in the
        # version directory or in product sub-directories beneath it
        parts = os.path.relpath(root, directory).split(os.sep)
        published = any(part in sc.PUBLISHED_VERSIONS for part in parts)
        for file in files:
            if file.endswith('.json') and published:
                with open(root + "/" + file, "r") as eventFile:
                    data = json.load(eventFile)

                    # Skip processing if domain contains "Deprecated"
                    if "domain" in data and "deprecated" in data["domain"].lower():
                        continue

                    domain = parts[1]
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
                                "description": event["description"],
                                "releaseStatus": event["releaseStatus"]
                            })
                            

                    for metric in data.get(sc.METRICS, []):
                        if isinstance(metric, dict) and "name" in metric and "releaseStatus" in metric:
                            dataLoaderStructure[domain][sc.METRICS].append({
                                "name": metric["name"],
                                "description": metric["description"],
                                "releaseStatus": metric["releaseStatus"]
                            })
                            
                    for alert in data.get(sc.ALERTS, []):
                        if isinstance(alert, dict) and "name" in alert and "releaseStatus" in alert:
                            dataLoaderStructure[domain][sc.ALERTS].append({
                                "name": alert["name"],
                                "description": alert["description"],
                                "releaseStatus": alert["releaseStatus"]
                            })
                            
    # successive versions of a domain redeclare the same names, so collapse each
    # section down to one entry per name
    for sections in dataLoaderStructure.values():
        for section, entries in sections.items():
            sections[section] = sorted(
                {entry["name"]: entry for entry in entries}.values(),
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
