import os
import json
import script_constants as sc

def main():
    supportedEvents = retrieve_supported_events()
    writeSupportedEventsToDataLoaderFile(supportedEvents)


def filterName(listOfDicts):
    return [d["name"] for d in listOfDicts]

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
                    dataLoaderStructure[domain][sc.EVENTS][sc.RELEASED].extend(filterName(data[sc.EVENTS][sc.RELEASED]))
                    dataLoaderStructure[domain][sc.EVENTS][sc.PREVIEW].extend(filterName(data[sc.EVENTS][sc.PREVIEW]))
                    dataLoaderStructure[domain][sc.METRICS][sc.RELEASED].extend(filterName(data[sc.METRICS][sc.RELEASED]))
                    dataLoaderStructure[domain][sc.METRICS][sc.PREVIEW].extend(filterName(data[sc.METRICS][sc.PREVIEW]))
                    dataLoaderStructure[domain][sc.ALERTS][sc.RELEASED].extend(filterName(data[sc.ALERTS][sc.RELEASED]))
                    dataLoaderStructure[domain][sc.ALERTS][sc.PREVIEW].extend(filterName(data[sc.ALERTS][sc.PREVIEW]))

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
