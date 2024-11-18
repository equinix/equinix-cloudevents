# Equinix CloudEvents

Equinix published [CloudEvent](https://cloudevents.io/) Types

Definitive "source of truth" for the Equinix Interconnection Observability event data formats

## CloudEvents in this repository

The following data payloads are the supported events and formats for Equinix Interconnection Observability

<!-- CATALOG_GENERATION_START -->
### Equinix Fabric ChangeAlert
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/ChangeAlert.json)
#### Data Type
`equinix.events.fabric.v1.ChangeAlert`
#### CloudEvent Type(s)


### Equinix Fabric ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/ChangeEvent.json)
#### Data Type
`equinix.events.fabric.v1.ChangeEvent`
#### CloudEvent Type(s)
`equinix.fabric.router.state.provisioning`<br>
`equinix.fabric.router.state.provisioned`<br>
`equinix.fabric.router.state.reprovisioning`<br>
`equinix.fabric.router.state.deprovisioning`<br>
`equinix.fabric.router.state.deprovisioned`<br>
`equinix.fabric.router.state.failed`<br>
`equinix.fabric.router.state.not_provisioned`<br>
`equinix.fabric.router.state.not_deprovisioned`<br>
`equinix.fabric.port.state.provisioned`<br>
`equinix.fabric.port.state.deprovisioned`<br>
`equinix.fabric.port.state.failed`<br>
`equinix.fabric.port.status.up`<br>
`equinix.fabric.port.status.down`<br>
`equinix.fabric.service_token.state.inactive`<br>
`equinix.fabric.service_token.state.deleted`<br>
`equinix.fabric.service_token.attribute.changed`<br>
`equinix.fabric.connection.state.pending`<br>
`equinix.fabric.connection.state.pending_interface_configuration`<br>
`equinix.fabric.connection.state.provisioning`<br>
`equinix.fabric.connection.state.provisioned`<br>
`equinix.fabric.connection.state.deprovisioning`<br>
`equinix.fabric.connection.state.deprovisioned`<br>
`equinix.fabric.connection.state.pending_approval`<br>
`equinix.fabric.connection.attribute.changed`<br>
`equinix.fabric.connection.status.up`<br>
`equinix.fabric.connection.status.down`<br>
`equinix.fabric.connection.bgpipv4_session_status.established`<br>
`equinix.fabric.connection.bgpipv4_session_status.idle`<br>
`equinix.fabric.connection.bgpipv4_session_status.connect`<br>
`equinix.fabric.connection.bgpipv6_session_status.established`<br>
`equinix.fabric.connection.bgpipv6_session_status.idle`<br>
`equinix.fabric.connection.bgpipv6_session_status.connect`<br>
`equinix.fabric.network.state.provisioning`<br>
`equinix.fabric.network.state.provisioned`<br>
`equinix.fabric.network.state.deprovisioning`<br>
`equinix.fabric.network.state.deprovisioned`

### Equinix Fabric MetricAlert
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/MetricAlert.json)
#### Data Type
`equinix.events.fabric.v1.MetricAlert`
#### CloudEvent Type(s)


### Equinix Fabric MetricEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/MetricEvent.json)
#### Data Type
`equinix.events.fabric.v1.MetricEvent`
#### CloudEvent Type(s)
`equinix.fabric.metric`
#### Metric Type(s)
`equinix.fabric.port.packets_erred_rx.count`<br>
`equinix.fabric.port.packets_erred_tx.count`<br>
`equinix.fabric.port.packets_dropped_rx.count`<br>
`equinix.fabric.port.packets_dropped_tx.count`<br>
`equinix.fabric.metro.{:asideMetroCode}_{:zsideMetroCode}.latency`<br>
`equinix.fabric.connection.bandwidth_rx.usage`<br>
`equinix.fabric.connection.bandwidth_tx.usage`<br>
`equinix.fabric.port.bandwidth_rx.usage`<br>
`equinix.fabric.port.bandwidth_tx.usage`
<!-- CATALOG_GENERATION_END -->
