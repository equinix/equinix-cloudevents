import os
import sys
import json

def find_json_files(directory):
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') and file != "catalog.json":
                json_files.append(os.path.join(root, file))
    return json_files

def retrieve_supported_events(files):
    events = set()
    for file in files:
        with open(file, "r") as eventFile:
            data = json.load(eventFile)
            for supportedEvent in data["cloudeventTypes"]:
                events.add(supportedEvent)

    return events

def writeSupportedEventsToDataLoaderFile(supportedEvents):
    with open("./SupportedEventTypes_DataLoader.json", "w") as eventsFile:
        eventsFile.write(json.dumps(sorted(supportedEvents), indent=4))
        eventsFile.write("\n")


if __name__ == "__main__":
    directory_to_search = sys.argv[1]
    json_files = find_json_files(directory_to_search)

    supportedEvents = retrieve_supported_events(json_files)
    writeSupportedEventsToDataLoaderFile(supportedEvents)
