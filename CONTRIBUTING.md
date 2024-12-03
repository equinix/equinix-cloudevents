# Equinix CloudEvents Contributors

Thanks for your interest! We're so glad you're here.

The Equinix CloudEvents Repo is a self-service contribution model that allows cross functional teams to manage their own
data schemas related to the CloudEvent types, metric names, and alert names that will be published from their team.

We follow the [CloudEvents](https://cloudevents.io/) project.

Every Data Schema is published to Github Pages through this repo on merges to the `main` branch. Contribution guidelines for
registration and promotion are provided in this document. Please read it thoroughly.

## Code of Conduct

Available via [https://github.com/equinix/equinix-cloudevents/blob/main/.github/CODE_OF_CONDUCT.md](https://github.com/equinix/equinix-cloudevents/blob/main/.github/CODE_OF_CONDUCT.md)

## Data Schema Gating through Equinix Event Manager

Each data schema is created to support CloudEvent types, metrics, and alerts. 
The team responsible for the data schema manages which environment the data schema is ready to support by managing the 
`cloudeventTypes`, `metricNames`, and `alertNames` attributes in the JSON. Each attribute is an object with list attributes 
`released` and `preview` that mark which environment the data schema is ready to suppport the given event/metric/alert in. Only 
place types in the `released` list if it is fully tested and ready for production. Place it into the `preview` list if it is under 
development and should only be available in UAT.
* `released` - attribute list under `cloudeventTypes`, `metricNames` and `alertNames` signifying that the name listed is fully tested and ready to be sent in production
* `preview` - attribute list under `cloudeventTypes`, `metricNames` and `alertNames` signifying that the name listed is under preview; meaning that the name is in development and should only be exposed to UAT

**Even if the data schema is not using metrics, or alerts, each attribute and sub attribute is required in the data schema. The Github Action will fail if they are not present and the Pull Request will not be merged.**

These lists are retrieved automatically via Github Actions to create a Data Loader that the Equinix Event Manager uses for event,
metric, and alert gating. **Contributing teams are fully responsible for managing these lists to ensure the proper gating is occuring for the Equinix Event Manager.**

Example of complete use case for the attributes:

```
...
 "cloudeventTypes": {
    "released": [
        "equinix.fabric.connection.ipv4_installed_routes.utilization",
        "equinix.fabric.connection.ipv6_installed_routes.utilization",
        "equinix.fabric.router.ipv4_installed_routes.utilization",
        "equinix.fabric.router.ipv6_installed_routes.utilization"
    ],
    "preview": []
},
"metricNames": {
    "released": [],
    "preview": []
},
"alertNames": {
    "released": [],
    "preview": []
}
...
```

## Registering a Data Schema

Each team will be adding data schemas in JSON format to their domain. The data schema will be used in the CloudEvent envelope to
specify the format of the data being streamed to customers.

The domains are added under `jsonschema/equinix` in the repository. Of the pattern `jsonschema/equinix/<domain>/<major_version>` with a full example being `jsonschema/equinix/fabric/v1`.

Each data schema is created to support CloudEvent types, metrics, and alerts. Please ensure the [Gating](#data-schema-gating-through-equinix-event-manager) section is read and properly understood to abide by those rules.

Each contributed data schema requires the following attributes:
* "$id" - The fully resolved URL to the data schema for linking from CloudEvent envelope and for generating Github Pages Site
* "name" - The name of the Data Schema being registered. Should match the file name
* "examples" - Provided examples of what the data schema could contain in a streamed event. Can be an empty list `[]` to start.
* "package" - The name of the package containing the data schema. Example: `equinix.fabric.v1`
* "datatype" - The full name of the datatype within the package. Example: `equinix.fabric.v1.ChangeEvent`
* "$schema" - The JSON Schema Specification used to draft the data schema. Use `"http://json-schema.org/draft-04/schema#"` for all
* "$ref" - The reference to the definition provided for the data schema. Example: `#/definitions/Data`
* "definitions" - The JSON Schema definition that describes the contents of the data schema for what will be contained in the event, metric, or alert that is supported by this data schema
* "cloudeventTypes" - Object with list attributes `released` and `preview` that mark which environment the data schema is ready to suppport the given event type in. Only place types in the `released` list if it is fully tested and ready for production. Place it into the `preview` list if it is under development and should only be available in UAT.
* "metricNames" - - Object with list attributes `released` and `preview` that mark which environment the data schema is ready to suppport the given metric in. Only place types in the `released` list if it is fully tested and ready for production. Place it into the `preview` list if it is under development and should only be available in UAT.
* "alertNames" - Object with list attributes `released` and `preview` that mark which environment the data schema is ready to suppport the given event type in. Only place types in the `released` list if it is fully tested and ready for production. Place it into the `preview` list if it is under development and should only be available in UAT.

## Data Schema Versioning

Versioning for data schemas is only based on major versions; there are no minor or patch versions. The major versions
are determined by the directory structure containing the data schema.

If no breaking changes (only additions, no modifications or deletions) are made to the data_schema when it is updated it can stay under the same major version; i.e. v1.

If a breaking change is made to the data_schema (deletion or modification) then it needs to be put into the next major version in a new version directory; i.e. v2.

Not all data_schemas need to be moved to v2. Just the ones that have breaking changes.

## Repository Versioning

The self service contribution model is setup to ensure the repo is always in a stable state that can be released to either UAT or production. Each time a Pull Request is merged into main a new version tag will be created based on SemVar for the commit names
present in the change. This tag will always be available to the Equinix Event Manager for releases. This setup is possible because of our CODEOWNERSHIP model.

## CODEOWNERS

CODEOWNERS file will be in place to establish a Github team (Synced with Equinix IAM) responsible for the files along the domain path they are contributing to. This ensures that 1 member from each domain team and 1 architect will always be necessary to approve a Pull Request before it can be merged.

This is critical because the responsibility of maintaining the `released` and `preview` lists outlined in the [Gating](#data-schema-gating-through-equinix-event-manager) section lies with the Domain owners and not the architects. Should any production defect be found the Domain owner is responsible for resolution