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

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>equinix.access_manager.user.role.added</td>
		<td>Role assignment event</td>
	</tr>
	<tr>
		<td>equinix.access_manager.user.role.removed</td>
		<td>Role unassignment event</td>
	</tr>
</table>

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

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>equinix.fabric.connection.attribute.changed</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.connect</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.established</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.idle</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.open_confirm</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.open_sent</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv6_session_status.connect</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv6_session_status.established</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv6_session_status.idle</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.deprovisioned</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.deprovisioning</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.pending</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.provisioned</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.provisioning</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.status.down</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.status.up</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.deprovisioned</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.deprovisioning</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.provisioned</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.provisioning</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.deprovisioned</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.failed</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.provisioned</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.status.down</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.status.up</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.deprovisioned</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.deprovisioning</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.failed</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.not_deprovisioned</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.not_provisioned</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.provisioned</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.provisioning</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.reprovisioning</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.attribute.changed</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.state.deleted</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.state.inactive</td>
		<td></td>
	</tr>
</table>

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

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>equinix.fabric.connection.ipv4_installed_routes.utilization</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.ipv6_installed_routes.utilization</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.ipv4_installed_routes.utilization</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.ipv6_installed_routes.utilization</td>
		<td></td>
	</tr>
</table>

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

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>equinix.fabric.metric</td>
		<td></td>
	</tr>
</table>

</details>

#### Metrics

<details>
<summary>Released</summary>

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bandwidth_rx.usage</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bandwidth_tx.usage</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.am_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.at_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ba_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bg_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bl_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bo_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bx_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ca_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ch_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cl_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cu_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.da_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.db_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dc_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.de_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dx_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.fr_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.gv_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.he_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hh_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hk_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ho_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.il_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jh_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ka_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.kl_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.la_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ld_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.lm_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ls_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ma_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mb_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.md_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.me_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mi_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ml_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mo_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mt_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mu_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mx_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ny_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.os_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ot_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pa_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pe_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ph_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.rj_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.se_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sg_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sk_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sl_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.so_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sp_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.st_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sv_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sy_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.tr_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ty_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.va_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wa_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wi_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.zh_{:metroCode}.latency</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.bandwidth_rx.usage</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.bandwidth_tx.usage</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_dropped_rx.count</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_dropped_tx.count</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_erred_rx.count</td>
		<td></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_erred_tx.count</td>
		<td></td>
	</tr>
</table>

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
