# Equinix CloudEvents

Equinix published [CloudEvent](https://cloudevents.io/) Types

Definitive "source of truth" for the Equinix Interconnection Observability event data formats

## CloudEvents in this repository

The following data payloads are the supported events and formats for Equinix Interconnection Observability

<!-- CATALOG_GENERATION_START -->
---
### Equinix Access Manager RoleAssignmentEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/access_manager/v1/RoleAssignmentEvent.json)
#### Data Type
`equinix.access_manager.v1.RoleAssignmentEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<details>
<summary>In Preview</summary>

`equinix.access_manager.user.role.added` <br>
`equinix.access_manager.user.role.removed`

</details>




---
### Equinix Fabric ChangeAlert
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/ChangeAlert.json)
#### Data Type
`equinix.fabric.v1.ChangeAlert`
#### Supported Events, Metrics, and Alerts



---
### Equinix Fabric ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/ChangeEvent.json)
#### Data Type
`equinix.fabric.v1.ChangeEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<details>
<summary>Released</summary>

`equinix.fabric.connection.attribute.changed` <br>
`equinix.fabric.connection.bgpipv4_session_status.connect` <br>
`equinix.fabric.connection.bgpipv4_session_status.established` <br>
`equinix.fabric.connection.bgpipv4_session_status.idle` <br>
`equinix.fabric.connection.bgpipv4_session_status.open_confirm` <br>
`equinix.fabric.connection.bgpipv4_session_status.open_sent` <br>
`equinix.fabric.connection.bgpipv6_session_status.connect` <br>
`equinix.fabric.connection.bgpipv6_session_status.established` <br>
`equinix.fabric.connection.bgpipv6_session_status.idle` <br>
`equinix.fabric.connection.state.deprovisioned` <br>
`equinix.fabric.connection.state.deprovisioning` <br>
`equinix.fabric.connection.state.pending` <br>
`equinix.fabric.connection.state.provisioned` <br>
`equinix.fabric.connection.state.provisioning` <br>
`equinix.fabric.connection.status.down` <br>
`equinix.fabric.connection.status.up` <br>
`equinix.fabric.network.state.deprovisioned` <br>
`equinix.fabric.network.state.deprovisioning` <br>
`equinix.fabric.network.state.provisioned` <br>
`equinix.fabric.network.state.provisioning` <br>
`equinix.fabric.port.state.deprovisioned` <br>
`equinix.fabric.port.state.failed` <br>
`equinix.fabric.port.state.provisioned` <br>
`equinix.fabric.port.status.down` <br>
`equinix.fabric.port.status.up` <br>
`equinix.fabric.router.state.deprovisioned` <br>
`equinix.fabric.router.state.deprovisioning` <br>
`equinix.fabric.router.state.failed` <br>
`equinix.fabric.router.state.not_deprovisioned` <br>
`equinix.fabric.router.state.not_provisioned` <br>
`equinix.fabric.router.state.provisioned` <br>
`equinix.fabric.router.state.provisioning` <br>
`equinix.fabric.router.state.reprovisioning` <br>
`equinix.fabric.service_token.attribute.changed` <br>
`equinix.fabric.service_token.state.deleted` <br>
`equinix.fabric.service_token.state.inactive`

</details>



---
### Equinix Fabric MetricAlert
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/MetricAlert.json)
#### Data Type
`equinix.fabric.v1.MetricAlert`
#### Supported Events, Metrics, and Alerts
#### Events

<details>
<summary>Released</summary>

`equinix.fabric.connection.ipv4_installed_routes.utilization` <br>
`equinix.fabric.connection.ipv6_installed_routes.utilization` <br>
`equinix.fabric.router.ipv4_installed_routes.utilization` <br>
`equinix.fabric.router.ipv6_installed_routes.utilization`

</details>



---
### Equinix Fabric MetricEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/MetricEvent.json)
#### Data Type
`equinix.fabric.v1.MetricEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<details>
<summary>Released</summary>

`equinix.fabric.metric`

</details>

#### Metrics

<details>
<summary>Released</summary>

`equinix.fabric.connection.bandwidth_rx.usage` <br>
`equinix.fabric.connection.bandwidth_tx.usage` <br>
`equinix.fabric.metro.am_{:metroCode}.latency` <br>
`equinix.fabric.metro.at_{:metroCode}.latency` <br>
`equinix.fabric.metro.ba_{:metroCode}.latency` <br>
`equinix.fabric.metro.bg_{:metroCode}.latency` <br>
`equinix.fabric.metro.bl_{:metroCode}.latency` <br>
`equinix.fabric.metro.bo_{:metroCode}.latency` <br>
`equinix.fabric.metro.bx_{:metroCode}.latency` <br>
`equinix.fabric.metro.ca_{:metroCode}.latency` <br>
`equinix.fabric.metro.ch_{:metroCode}.latency` <br>
`equinix.fabric.metro.cl_{:metroCode}.latency` <br>
`equinix.fabric.metro.cu_{:metroCode}.latency` <br>
`equinix.fabric.metro.da_{:metroCode}.latency` <br>
`equinix.fabric.metro.db_{:metroCode}.latency` <br>
`equinix.fabric.metro.dc_{:metroCode}.latency` <br>
`equinix.fabric.metro.de_{:metroCode}.latency` <br>
`equinix.fabric.metro.dx_{:metroCode}.latency` <br>
`equinix.fabric.metro.fr_{:metroCode}.latency` <br>
`equinix.fabric.metro.gv_{:metroCode}.latency` <br>
`equinix.fabric.metro.he_{:metroCode}.latency` <br>
`equinix.fabric.metro.hh_{:metroCode}.latency` <br>
`equinix.fabric.metro.hk_{:metroCode}.latency` <br>
`equinix.fabric.metro.ho_{:metroCode}.latency` <br>
`equinix.fabric.metro.il_{:metroCode}.latency` <br>
`equinix.fabric.metro.jh_{:metroCode}.latency` <br>
`equinix.fabric.metro.ka_{:metroCode}.latency` <br>
`equinix.fabric.metro.kl_{:metroCode}.latency` <br>
`equinix.fabric.metro.la_{:metroCode}.latency` <br>
`equinix.fabric.metro.ld_{:metroCode}.latency` <br>
`equinix.fabric.metro.lm_{:metroCode}.latency` <br>
`equinix.fabric.metro.ls_{:metroCode}.latency` <br>
`equinix.fabric.metro.ma_{:metroCode}.latency` <br>
`equinix.fabric.metro.mb_{:metroCode}.latency` <br>
`equinix.fabric.metro.md_{:metroCode}.latency` <br>
`equinix.fabric.metro.me_{:metroCode}.latency` <br>
`equinix.fabric.metro.mi_{:metroCode}.latency` <br>
`equinix.fabric.metro.ml_{:metroCode}.latency` <br>
`equinix.fabric.metro.mo_{:metroCode}.latency` <br>
`equinix.fabric.metro.mt_{:metroCode}.latency` <br>
`equinix.fabric.metro.mu_{:metroCode}.latency` <br>
`equinix.fabric.metro.mx_{:metroCode}.latency` <br>
`equinix.fabric.metro.ny_{:metroCode}.latency` <br>
`equinix.fabric.metro.os_{:metroCode}.latency` <br>
`equinix.fabric.metro.ot_{:metroCode}.latency` <br>
`equinix.fabric.metro.pa_{:metroCode}.latency` <br>
`equinix.fabric.metro.pe_{:metroCode}.latency` <br>
`equinix.fabric.metro.ph_{:metroCode}.latency` <br>
`equinix.fabric.metro.rj_{:metroCode}.latency` <br>
`equinix.fabric.metro.se_{:metroCode}.latency` <br>
`equinix.fabric.metro.sg_{:metroCode}.latency` <br>
`equinix.fabric.metro.sk_{:metroCode}.latency` <br>
`equinix.fabric.metro.sl_{:metroCode}.latency` <br>
`equinix.fabric.metro.so_{:metroCode}.latency` <br>
`equinix.fabric.metro.sp_{:metroCode}.latency` <br>
`equinix.fabric.metro.st_{:metroCode}.latency` <br>
`equinix.fabric.metro.sv_{:metroCode}.latency` <br>
`equinix.fabric.metro.sy_{:metroCode}.latency` <br>
`equinix.fabric.metro.tr_{:metroCode}.latency` <br>
`equinix.fabric.metro.ty_{:metroCode}.latency` <br>
`equinix.fabric.metro.va_{:metroCode}.latency` <br>
`equinix.fabric.metro.wa_{:metroCode}.latency` <br>
`equinix.fabric.metro.wi_{:metroCode}.latency` <br>
`equinix.fabric.metro.zh_{:metroCode}.latency` <br>
`equinix.fabric.port.bandwidth_rx.usage` <br>
`equinix.fabric.port.bandwidth_tx.usage` <br>
`equinix.fabric.port.packets_dropped_rx.count` <br>
`equinix.fabric.port.packets_dropped_tx.count` <br>
`equinix.fabric.port.packets_erred_rx.count` <br>
`equinix.fabric.port.packets_erred_tx.count`

</details>


---
### Equinix Identity ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/identity/v1/ChangeEvent.json)
#### Data Type
`equinix.identity.v1.ChangeEvent`
#### Supported Events, Metrics, and Alerts



---
### Equinix Network Edge ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/network_edge/v1/ChangeEvent.json)
#### Data Type
`equinix.network_edge.v1.ChangeEvent`
#### Supported Events, Metrics, and Alerts



---
### Equinix Resource Manager ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/resource_manager/v1/ChangeEvent.json)
#### Data Type
`equinix.resource_manager.v1.ChangeEvent`
#### Supported Events, Metrics, and Alerts



<!-- CATALOG_GENERATION_END -->
