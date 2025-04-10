# Equinix CloudEvents Contributors

Thanks for your interest! We're so glad you're here.

The Equinix CloudEvents Repo is a self-service contribution model that allows cross functional teams to manage their own
data schemas related to the CloudEvent types, metric names, and alert names that will be published from their team.

We follow the [CloudEvents](https://cloudevents.io/) project.

Every Data Schema is published to Github Pages through this repo on merges to the `main` branch. Contribution guidelines
for registration and promotion are provided in this document. Please read it thoroughly.

## Code of Conduct

Available via [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)

## Data Schema Gating through Equinix Event Manager

Each data schema is created to support CloudEvent types, metrics, and alerts. The team responsible for the data schema
manages which environment the data schema is ready to support by managing the `cloudeventTypes`, `metricNames`, and
`alertNames` attributes in the JSON. Each attribute contains a list of object with the following attributes: 

* `name` - The name of the CloudEvents type, Metric or Alert
* `description` = A breif description of the event, metric or alert
* `sloCategoryCode` - This attribute signifies the SLO category code associated with the event, metric or alert
* `releaseStatus` - Set as `released` under `cloudeventTypes`,`metricNames` and `alertNames` if the name listed is fully
  tested and ready to be sent in production
* `releaseStatus` - Set as `preview` under `cloudeventTypes`, `metricNames` and `alertNames` if the name listed is under
preview; meaning that the name is in development and should only be exposed to DEV enviornment

**Even if the data schema is not using metrics, or alerts, each attribute and sub attribute is required in the data
schema. The Github Action will fail if they are not present and the Pull Request will not be merged.**

These lists are retrieved automatically via Github Actions to create a Data Loader that the Equinix Event Manager uses
for event, metric, and alert gating. **Contributing teams are fully responsible for managing these lists to ensure the
proper gating is occuring for the Equinix Event Manager.**

Example of complete use case for the attributes:

```
...
 "cloudeventTypes": [
    {
        "name": "equinix.fabric.connection.ipv4_installed_routes.utilization",
        "descrption": "Fabric connection ipv4 installed routes utilization",
        "sloCategoryCode": "DATA_PATH"
        "releaseStatus": "released"
    },
    {
        "name": "equinix.fabric.connection.ipv6_installed_routes.utilization",
        "descrption": "Fabric connection ipv4 installed routes utilization",
        "sloCategoryCode": "METRO_LATENCY"
        "releaseStatus": "preview",
    },
],
"metricNames": [],
"alertNames": []
...
```
## Process for Updating Cloud Events SLO
Contributors must update the /jsonschema/sloCategories.json file when adding a new sloCategoryCode to the data schema.
This file contains three lists:
* eventsSLO
* metricsSLO
* alertsSLO

Each SLO category entry should include following attributes:
```
...
{
    "category": "Datapath Metric SLO",
    "code": "RED_METRIC_SLO",
    "reportingInterval": "PT300S",
    "reportingLatencyMax": "PT720S",
    "streamingLatencyMax": "PT60S",
    "queryLatencyMax": "PT4S",
    "orignalDataRetention": "PT90D",
    "1HAggregationRetention": "PT365D",
    "1DAggregationRetention": "PT1095D"
}
...
```
Each SLO category and code must be appropriately added to ensure accurate tracking and performance measurement.

## Registering a Data Schema

Each team will be adding data schemas in JSON format to their domain. The data schema will be used in the CloudEvent
envelope to specify the format of the data being streamed to customers.

The domains are added under `jsonschema/equinix` in the repository. Of the pattern
`jsonschema/equinix/<domain>/<major_version>` with a full example being `jsonschema/equinix/fabric/v1`.

Each data schema is created to support CloudEvent types, metrics, and alerts. Please ensure the
[Gating](#data-schema-gating-through-equinix-event-manager) section is read and properly understood to abide by those
rules.

Each contributed data schema requires the following attributes:
* "$id" - The fully resolved URL to the data schema for linking from CloudEvent envelope and for generating Github Pages
 Site
* "name" - The name of the Data Schema being registered. Should match the file name
* "examples" - Provided examples of what the data schema could contain in a streamed event. Can be an empty list `[]` to
start.
* "package" - The name of the package containing the data schema. Example: `equinix.fabric.v1`
* "datatype" - The full name of the datatype within the package. Example: `equinix.fabric.v1.ChangeEvent`
* "$schema" - The JSON Schema Specification used to draft the data schema. Use
`"http://json-schema.org/draft-04/schema#"` for all
* "$ref" - The reference to the definition provided for the data schema. Example: `#/definitions/Data`
* "definitions" - The JSON Schema definition that describes the contents of the data schema for what will be contained
 in the event, metric, or alert that is supported by this data schema
* "cloudeventTypes" - List of object with attribute `releaseStatus` that mark which environment the data schema is ready
 to suppport the given event type in. Mark `releaseStatus` as `released` if it is fully tested and ready for production.
 Mark `releaseStatus` as `preview` if it is under development and should only be available in DEV enviornment.
* "metricNames" - List of object with attributes `releaseStatus` that mark which environment the data schema is ready to
 suppport the given event type in. Mark `releaseStatus` as `released` if it is fully tested and ready for production.
 Mark `releaseStatus` as `preview` if it is under development and should only be available in DEV enviornment.
* "alertNames" - List of object with attributes `releaseStatus` that mark which environment the data schema is ready to
 suppport the given event type in. Mark `releaseStatus` as `released` if it is fully tested and ready for production.
 Mark `releaseStatus` as `preview` if it is under development and should only be available in DEV enviornment.

## Process for Upgrading Event/Metric/Alert from Development to Production

When adding a new event/metric/alert to a data schema always start by marking `releaseStatus` as `preview`. This
identifies *in development* items and is the starting point for new events/metrics/alerts being added into the repo.

Once an event/metric/alert has been thoroughly tested in lower environments you will mark `releaseStatus` as `released`.
This indicates that your item is ready to be consumed in production and the production Equinix Event Manager will pass
these items through to the consumers.

It is imperative that you understand the responsibility involved for managing your team's domain with regards to the
`releaseStatus` attribute in your data schema files. The [CODEOWNERS](#codeowners) section describes how responsibility
is managed within the repo. Please review it thoroughly.

## CODEOWNERS

CODEOWNERS file will be in place to establish a Github team (Synced with Equinix IAM) responsible for the files along
the domain path they are contributing to. This ensures that 1 member from each domain team and 1 architect will always
be necessary to approve a Pull Request before it can be merged.

This is critical because the responsibility of maintaining the `releaseStatus` and `sloCategoryCode` attributes outlined
in the [Gating](#data-schema-gating-through-equinix-event-manager) section lies with the Domain owners and not the
architects. Should any production defect be found the Domain owner is responsible for resolution

When adding a new domain to the `jsonschema/equinix` directory, add an entry to the CODEOWNERS file signifying which
Github Team is responsible for reviewing/approving PRs that modify the domain directory being added

## Data Schema Versioning

Versioning for data schemas is only based on major versions; there are no minor or patch versions. The major versions
are determined by the directory structure containing the data schema.

If no breaking changes (only additions, no modifications or deletions) are made to the data_schema when it is updated it
can stay under the same major version; i.e. v1.

If a breaking change is made to the data_schema (deletion or modification) then it needs to be put into the next major
version in a new version directory; i.e. v2.

Not all data_schemas need to be moved to v2. Just the ones that have breaking changes.

## Repository Versioning

The self service contribution model is setup to ensure the repo is always in a stable state that can be released to
either DEV or production enviornment. Each time a Pull Request is merged into main a new version tag will be created
based on SemVar for the commit names present in the change. This tag will always be available to the Equinix Event
Manager for releases. This setup is possible because of our CODEOWNERSHIP model.
