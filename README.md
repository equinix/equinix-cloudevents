# Equinix CloudEvents

Equinix published [CloudEvent](https://cloudevents.io/) Types

Definitive "source of truth" for the Equinix Interconnection Observability event data formats

## CloudEvents in this repository

The following data payloads are the supported events and formats for Equinix Interconnection Observability

<!-- CATALOG_GENERATION_START -->
---
### Equinix Access Manager ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/access_manager/v1/ChangeEvent.json)
#### Data Type
`equinix.access_manager.v1.ChangeEvent`
#### Supported Events, Metrics, and Alerts



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

| Name | Description |

|equinix.fabric.connection.attribute.changed||
|equinix.fabric.connection.bgpipv4_session_status.connect||
|equinix.fabric.connection.bgpipv4_session_status.established||
|equinix.fabric.connection.bgpipv4_session_status.idle||
|equinix.fabric.connection.bgpipv4_session_status.open_confirm||
|equinix.fabric.connection.bgpipv4_session_status.open_sent||
|equinix.fabric.connection.bgpipv6_session_status.connect||
|equinix.fabric.connection.bgpipv6_session_status.established||
|equinix.fabric.connection.bgpipv6_session_status.idle||
|equinix.fabric.connection.state.deprovisioned||
|equinix.fabric.connection.state.deprovisioning||
|equinix.fabric.connection.state.pending||
|equinix.fabric.connection.state.provisioned||
|equinix.fabric.connection.state.provisioning||
|equinix.fabric.connection.status.down||
|equinix.fabric.connection.status.up||
|equinix.fabric.network.state.deprovisioned||
|equinix.fabric.network.state.deprovisioning||
|equinix.fabric.network.state.provisioned||
|equinix.fabric.network.state.provisioning||
|equinix.fabric.port.state.deprovisioned||
|equinix.fabric.port.state.failed||
|equinix.fabric.port.state.provisioned||
|equinix.fabric.port.status.down||
|equinix.fabric.port.status.up||
|equinix.fabric.router.state.deprovisioned||
|equinix.fabric.router.state.deprovisioning||
|equinix.fabric.router.state.failed||
|equinix.fabric.router.state.not_deprovisioned||
|equinix.fabric.router.state.not_provisioned||
|equinix.fabric.router.state.provisioned||
|equinix.fabric.router.state.provisioning||
|equinix.fabric.router.state.reprovisioning||
|equinix.fabric.service_token.attribute.changed||
|equinix.fabric.service_token.state.deleted||
|equinix.fabric.service_token.state.inactive||

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

| Name | Description |

|equinix.fabric.connection.ipv4_installed_routes.utilization||
|equinix.fabric.connection.ipv6_installed_routes.utilization||
|equinix.fabric.router.ipv4_installed_routes.utilization||
|equinix.fabric.router.ipv6_installed_routes.utilization||

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

| Name | Description |

|equinix.fabric.metric||

</details>

#### Metrics

<details>
<summary>Released</summary>

| Name | Description |

|equinix.fabric.connection.bandwidth_rx.usage||
|equinix.fabric.connection.bandwidth_tx.usage||
|equinix.fabric.metro.am_{:metroCode}.latency||
|equinix.fabric.metro.at_{:metroCode}.latency||
|equinix.fabric.metro.ba_{:metroCode}.latency||
|equinix.fabric.metro.bg_{:metroCode}.latency||
|equinix.fabric.metro.bl_{:metroCode}.latency||
|equinix.fabric.metro.bo_{:metroCode}.latency||
|equinix.fabric.metro.bx_{:metroCode}.latency||
|equinix.fabric.metro.ca_{:metroCode}.latency||
|equinix.fabric.metro.ch_{:metroCode}.latency||
|equinix.fabric.metro.cl_{:metroCode}.latency||
|equinix.fabric.metro.cu_{:metroCode}.latency||
|equinix.fabric.metro.da_{:metroCode}.latency||
|equinix.fabric.metro.db_{:metroCode}.latency||
|equinix.fabric.metro.dc_{:metroCode}.latency||
|equinix.fabric.metro.de_{:metroCode}.latency||
|equinix.fabric.metro.dx_{:metroCode}.latency||
|equinix.fabric.metro.fr_{:metroCode}.latency||
|equinix.fabric.metro.gv_{:metroCode}.latency||
|equinix.fabric.metro.he_{:metroCode}.latency||
|equinix.fabric.metro.hh_{:metroCode}.latency||
|equinix.fabric.metro.hk_{:metroCode}.latency||
|equinix.fabric.metro.ho_{:metroCode}.latency||
|equinix.fabric.metro.il_{:metroCode}.latency||
|equinix.fabric.metro.jh_{:metroCode}.latency||
|equinix.fabric.metro.ka_{:metroCode}.latency||
|equinix.fabric.metro.kl_{:metroCode}.latency||
|equinix.fabric.metro.la_{:metroCode}.latency||
|equinix.fabric.metro.ld_{:metroCode}.latency||
|equinix.fabric.metro.lm_{:metroCode}.latency||
|equinix.fabric.metro.ls_{:metroCode}.latency||
|equinix.fabric.metro.ma_{:metroCode}.latency||
|equinix.fabric.metro.mb_{:metroCode}.latency||
|equinix.fabric.metro.md_{:metroCode}.latency||
|equinix.fabric.metro.me_{:metroCode}.latency||
|equinix.fabric.metro.mi_{:metroCode}.latency||
|equinix.fabric.metro.ml_{:metroCode}.latency||
|equinix.fabric.metro.mo_{:metroCode}.latency||
|equinix.fabric.metro.mt_{:metroCode}.latency||
|equinix.fabric.metro.mu_{:metroCode}.latency||
|equinix.fabric.metro.mx_{:metroCode}.latency||
|equinix.fabric.metro.ny_{:metroCode}.latency||
|equinix.fabric.metro.os_{:metroCode}.latency||
|equinix.fabric.metro.ot_{:metroCode}.latency||
|equinix.fabric.metro.pa_{:metroCode}.latency||
|equinix.fabric.metro.pe_{:metroCode}.latency||
|equinix.fabric.metro.ph_{:metroCode}.latency||
|equinix.fabric.metro.rj_{:metroCode}.latency||
|equinix.fabric.metro.se_{:metroCode}.latency||
|equinix.fabric.metro.sg_{:metroCode}.latency||
|equinix.fabric.metro.sk_{:metroCode}.latency||
|equinix.fabric.metro.sl_{:metroCode}.latency||
|equinix.fabric.metro.so_{:metroCode}.latency||
|equinix.fabric.metro.sp_{:metroCode}.latency||
|equinix.fabric.metro.st_{:metroCode}.latency||
|equinix.fabric.metro.sv_{:metroCode}.latency||
|equinix.fabric.metro.sy_{:metroCode}.latency||
|equinix.fabric.metro.tr_{:metroCode}.latency||
|equinix.fabric.metro.ty_{:metroCode}.latency||
|equinix.fabric.metro.va_{:metroCode}.latency||
|equinix.fabric.metro.wa_{:metroCode}.latency||
|equinix.fabric.metro.wi_{:metroCode}.latency||
|equinix.fabric.metro.zh_{:metroCode}.latency||
|equinix.fabric.port.bandwidth_rx.usage||
|equinix.fabric.port.bandwidth_tx.usage||
|equinix.fabric.port.packets_dropped_rx.count||
|equinix.fabric.port.packets_dropped_tx.count||
|equinix.fabric.port.packets_erred_rx.count||
|equinix.fabric.port.packets_erred_tx.count||

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
