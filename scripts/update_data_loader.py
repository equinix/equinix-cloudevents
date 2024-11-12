import os
import json

def retrieve_supported_events():
    directory = os.path.dirname(os.path.abspath(__file__)) + '/../jsonschema'
    events = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') and file != "catalog.json":
                with open(root + "/" + file, "r") as eventFile:
                    data = json.load(eventFile)
                    events.update(data["cloudeventTypes"])
    return events

def writeSupportedEventsToDataLoaderFile(supportedEvents):
    with open("./SupportedEventTypes_DataLoader.json", "w") as eventsFile:
        eventsFile.write(json.dumps(sorted(supportedEvents), indent=4))
        eventsFile.write("\n")


if __name__ == "__main__":
    supportedEvents = retrieve_supported_events()
    writeSupportedEventsToDataLoaderFile(supportedEvents)
