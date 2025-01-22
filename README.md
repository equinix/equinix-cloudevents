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
<summary>Released</summary>

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
		<td>Connection named ${connection_name} attributes are changed</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.active</td>
		<td>Neighbor ${IP} address session state changed to Active</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.connect</td>
		<td>Neighbor ${IP} address session state changed to Connect</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.established</td>
		<td>Neighbor ${IP} address session state changed to Established</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.idle</td>
		<td>Neighbor ${IP} address session state changed to Idle</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.open_confirm</td>
		<td>Neighbor ${IP} address session state changed to Open_confirm</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv4_session_status.open_sent</td>
		<td>Neighbor ${IP} address session state changed to Open_sent</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv6_session_status.active</td>
		<td>Neighbor ${IP} address session state changed to Active</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv6_session_status.connect</td>
		<td>Neighbor ${IP} address session state changed to Connect</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv6_session_status.established</td>
		<td>Neighbor ${IP} address session state changed to Established</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv6_session_status.idle</td>
		<td>Neighbor ${IP} address session state changed to Idle</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv6_session_status.open_confirm</td>
		<td>Neighbor ${IP} address session state changed to Open_confirm</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bgpipv6_session_status.open_sent</td>
		<td>Neighbor ${IP} address session state changed to open_sent</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.deprovisioned</td>
		<td>Connection named ${connection_name} state changed to deprovisioned</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.deprovisioning</td>
		<td>Connection named ${connection_name} state changed to deprovisioning</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.pending</td>
		<td>Connection named ${connection_name} state changed to pending</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.provisioned</td>
		<td>Connection named ${connection_name} state changed to provisioned</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.provisioning</td>
		<td>Connection named ${connection_name} state changed to provisioning</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.status.down</td>
		<td>Connection '${connection_name}' status changed to DOWN</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.status.up</td>
		<td>Connection '${connection_name}' status changed to UP</td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.deprovisioned</td>
		<td>Network named ${network_name} state changed to deprovisioned</td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.deprovisioning</td>
		<td>Network named ${network_name} state changed to deprovisioning</td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.provisioned</td>
		<td>Network named ${network_name} state changed to provisioned</td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.provisioning</td>
		<td>Network named ${network_name} state changed to provisioning</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.deprovisioned</td>
		<td>Virtual port named ${port_name} state changed to deprovisioned</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.failed</td>
		<td>Virtual port named ${port_name} state changed to failed</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.provisioned</td>
		<td>Virtual port named ${port_name} state changed to provisioned</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.status.down</td>
		<td>Virtual|Physical port '${port_name}' status changed to DOWN</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.status.up</td>
		<td>Virtual|Physical port '${port_name}' status changed to UP</td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.deprovisioned</td>
		<td>Router named ${router_name} successfully deprovisioned</td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.deprovisioning</td>
		<td>Router named ${router_name} state changed to deprovisioning</td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.failed</td>
		<td>Router named ${router_name} state changed to failed</td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.not_deprovisioned</td>
		<td>Router named ${router_name} state changed to not_deprovisioned</td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.not_provisioned</td>
		<td>Router named ${router_name} state changed to not_provisioned</td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.provisioned</td>
		<td>Router named ${router_name} successfully provisioned</td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.provisioning</td>
		<td>Router named ${router_name} state changed to provisioning</td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.reprovisioning</td>
		<td>Router named ${router_name} state changed to reprovisioning</td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.attribute.changed</td>
		<td>Token successfully updated</td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.resend_email_notification.failed</td>
		<td>Token resend email notification failed</td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.resend_email_notification.succeeded</td>
		<td>Token resend email notification succeeded</td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.state.deleted</td>
		<td>Token successfully deleted</td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.state.inactive</td>
		<td>Token successfully created</td>
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
<summary>In Preview</summary>

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bandwidth_rx.usage</td>
		<td>Connection inbound bandwidth usage above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bandwidth_tx.usage</td>
		<td>Connection outbound bandwidth usage above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.bandwidth_rx.usage</td>
		<td>Port inbound bandwidth usage above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.bandwidth_tx.usage</td>
		<td>Port outbound bandwidth usage above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_dropped_rx.count</td>
		<td>Port inbound dropped packets count above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_dropped_tx.count</td>
		<td>Port outbound dropped packets count above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_erred_rx.count</td>
		<td>Port inbound erred packets count above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_erred_tx.count</td>
		<td>Port outbound erred packets count above ${threshold}</td>
	</tr>
</table>

</details>



<details>
<summary>Released</summary>

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>equinix.fabric.connection.installed_routes_ipv4.utilization</td>
		<td>Utilization of connection '${connection_name}' active IPv4 routes reached ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.installed_routes_ipv6.utilization</td>
		<td>Utilization of connection '${connection_name}' active IPv6 routes reached ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.router.installed_routes_ipv4.utilization</td>
		<td>Utilization of router '${router_name}' total IPv4 routes reached ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.router.installed_routes_ipv6.utilization</td>
		<td>Utilization of router '${router_name}' total IPv6 routes reached ${threshold}</td>
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
		<td>Connection inbound bandwidth usage in bit/sec</td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bandwidth_tx.usage</td>
		<td>Connection outbound bandwidth usage in bit/sec</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.bandwidth_rx.usage</td>
		<td>Port inbound bandwidth usage in bit/sec</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.bandwidth_tx.usage</td>
		<td>Port outbound bandwidth usage in bit/sec</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_dropped_rx.count</td>
		<td>Port inbound dropped packets count</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_dropped_tx.count</td>
		<td>Port outbound dropped packets count</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_erred_rx.count</td>
		<td>Port inbound erred packets count</td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_erred_tx.count</td>
		<td>Port outbound erred packets count</td>
	</tr>
</table>

</details>


---
### Equinix Fabric Metro Latency Alert
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/MetroLatencyAlert.json)
#### Data Type
`equinix.fabric.v1.MetroLatencyAlert`
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
		<td>equinix.fabric.metro.am_{metroCode}.latency</td>
		<td>Metro latency from AM to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.at_{metroCode}.latency</td>
		<td>Metro latency from AT to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ba_{metroCode}.latency</td>
		<td>Metro latency from BA to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bg_{metroCode}.latency</td>
		<td>Metro latency from BG to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bl_{metroCode}.latency</td>
		<td>Metro latency from BL to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bo_{metroCode}.latency</td>
		<td>Metro latency from BO to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bx_{metroCode}.latency</td>
		<td>Metro latency from BX to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ca_{metroCode}.latency</td>
		<td>Metro latency from CA to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ch_{metroCode}.latency</td>
		<td>Metro latency from CH to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cl_{metroCode}.latency</td>
		<td>Metro latency from CL to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cu_{metroCode}.latency</td>
		<td>Metro latency from CU to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.da_{metroCode}.latency</td>
		<td>Metro latency from DA to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.db_{metroCode}.latency</td>
		<td>Metro latency from DB to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dc_{metroCode}.latency</td>
		<td>Metro latency from DC to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.de_{metroCode}.latency</td>
		<td>Metro latency from DE to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dx_{metroCode}.latency</td>
		<td>Metro latency from DX to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.fr_{metroCode}.latency</td>
		<td>Metro latency from FR to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.gv_{metroCode}.latency</td>
		<td>Metro latency from GV to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.he_{metroCode}.latency</td>
		<td>Metro latency from HE to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hh_{metroCode}.latency</td>
		<td>Metro latency from HH to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hk_{metroCode}.latency</td>
		<td>Metro latency from HK to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ho_{metroCode}.latency</td>
		<td>Metro latency from HO to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.il_{metroCode}.latency</td>
		<td>Metro latency from IL to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jh_{metroCode}.latency</td>
		<td>Metro latency from JH to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ka_{metroCode}.latency</td>
		<td>Metro latency from KA to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.kl_{metroCode}.latency</td>
		<td>Metro latency from KL to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.la_{metroCode}.latency</td>
		<td>Metro latency from LA to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ld_{metroCode}.latency</td>
		<td>Metro latency from LD to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.lm_{metroCode}.latency</td>
		<td>Metro latency from LM to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ls_{metroCode}.latency</td>
		<td>Metro latency from LS to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ma_{metroCode}.latency</td>
		<td>Metro latency from MA to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mb_{metroCode}.latency</td>
		<td>Metro latency from MB to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.md_{metroCode}.latency</td>
		<td>Metro latency from MD to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.me_{metroCode}.latency</td>
		<td>Metro latency from ME to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mi_{metroCode}.latency</td>
		<td>Metro latency from MI to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ml_{metroCode}.latency</td>
		<td>Metro latency from ML to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mo_{metroCode}.latency</td>
		<td>Metro latency from MO to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mt_{metroCode}.latency</td>
		<td>Metro latency from MT to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mu_{metroCode}.latency</td>
		<td>Metro latency from MU to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mx_{metroCode}.latency</td>
		<td>Metro latency from MX to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ny_{metroCode}.latency</td>
		<td>Metro latency from NY to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.os_{metroCode}.latency</td>
		<td>Metro latency from OS to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ot_{metroCode}.latency</td>
		<td>Metro latency from OT to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pa_{metroCode}.latency</td>
		<td>Metro latency from PA to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pe_{metroCode}.latency</td>
		<td>Metro latency from PE to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ph_{metroCode}.latency</td>
		<td>Metro latency from PH to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.rj_{metroCode}.latency</td>
		<td>Metro latency from RJ to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.se_{metroCode}.latency</td>
		<td>Metro latency from SE to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sg_{metroCode}.latency</td>
		<td>Metro latency from SG to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sk_{metroCode}.latency</td>
		<td>Metro latency from SK to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sl_{metroCode}.latency</td>
		<td>Metro latency from SL to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.so_{metroCode}.latency</td>
		<td>Metro latency from SO to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sp_{metroCode}.latency</td>
		<td>Metro latency from SP to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.st_{metroCode}.latency</td>
		<td>Metro latency from ST to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sv_{metroCode}.latency</td>
		<td>Metro latency from SV to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sy_{metroCode}.latency</td>
		<td>Metro latency from SY to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.tr_{metroCode}.latency</td>
		<td>Metro latency from TR to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ty_{metroCode}.latency</td>
		<td>Metro latency from TY to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.va_{metroCode}.latency</td>
		<td>Metro latency from VA to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wa_{metroCode}.latency</td>
		<td>Metro latency from WA to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wi_{metroCode}.latency</td>
		<td>Metro latency from WI to ${metroCode} above ${threshold}</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.zh_{metroCode}.latency</td>
		<td>Metro latency from ZH to ${metroCode} above ${threshold}</td>
	</tr>
</table>

</details>




---
### Equinix Fabric Metro Latency Metric
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/MetroLatencyMetric.json)
#### Data Type
`equinix.fabric.v1.MetroLatencyMetric`
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
		<td>equinix.fabric.metro.am_{metroCode}.latency</td>
		<td>Metro latency from AM to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.at_{metroCode}.latency</td>
		<td>Metro latency from AT to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ba_{metroCode}.latency</td>
		<td>Metro latency from BA to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bg_{metroCode}.latency</td>
		<td>Metro latency from BG to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bl_{metroCode}.latency</td>
		<td>Metro latency from BL to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bo_{metroCode}.latency</td>
		<td>Metro latency from BO to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bx_{metroCode}.latency</td>
		<td>Metro latency from BX to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ca_{metroCode}.latency</td>
		<td>Metro latency from CA to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ch_{metroCode}.latency</td>
		<td>Metro latency from CH to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cl_{metroCode}.latency</td>
		<td>Metro latency from CL to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cu_{metroCode}.latency</td>
		<td>Metro latency from CU to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.da_{metroCode}.latency</td>
		<td>Metro latency from DA to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.db_{metroCode}.latency</td>
		<td>Metro latency from DB to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dc_{metroCode}.latency</td>
		<td>Metro latency from DC to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.de_{metroCode}.latency</td>
		<td>Metro latency from DE to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dx_{metroCode}.latency</td>
		<td>Metro latency from DX to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.fr_{metroCode}.latency</td>
		<td>Metro latency from FR to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.gv_{metroCode}.latency</td>
		<td>Metro latency from GV to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.he_{metroCode}.latency</td>
		<td>Metro latency from HE to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hh_{metroCode}.latency</td>
		<td>Metro latency from HH to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hk_{metroCode}.latency</td>
		<td>Metro latency from HK to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ho_{metroCode}.latency</td>
		<td>Metro latency from HO to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.il_{metroCode}.latency</td>
		<td>Metro latency from IL to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jh_{metroCode}.latency</td>
		<td>Metro latency from JH to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ka_{metroCode}.latency</td>
		<td>Metro latency from KA to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.kl_{metroCode}.latency</td>
		<td>Metro latency from KL to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.la_{metroCode}.latency</td>
		<td>Metro latency from LA to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ld_{metroCode}.latency</td>
		<td>Metro latency from LD to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.lm_{metroCode}.latency</td>
		<td>Metro latency from LM to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ls_{metroCode}.latency</td>
		<td>Metro latency from LS to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ma_{metroCode}.latency</td>
		<td>Metro latency from MA to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mb_{metroCode}.latency</td>
		<td>Metro latency from MB to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.md_{metroCode}.latency</td>
		<td>Metro latency from MD to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.me_{metroCode}.latency</td>
		<td>Metro latency from ME to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mi_{metroCode}.latency</td>
		<td>Metro latency from MI to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ml_{metroCode}.latency</td>
		<td>Metro latency from ML to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mo_{metroCode}.latency</td>
		<td>Metro latency from MO to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mt_{metroCode}.latency</td>
		<td>Metro latency from MT to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mu_{metroCode}.latency</td>
		<td>Metro latency from MU to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mx_{metroCode}.latency</td>
		<td>Metro latency from MX to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ny_{metroCode}.latency</td>
		<td>Metro latency from NY to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.os_{metroCode}.latency</td>
		<td>Metro latency from OS to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ot_{metroCode}.latency</td>
		<td>Metro latency from OT to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pa_{metroCode}.latency</td>
		<td>Metro latency from PA to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pe_{metroCode}.latency</td>
		<td>Metro latency from PE to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ph_{metroCode}.latency</td>
		<td>Metro latency from PH to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.rj_{metroCode}.latency</td>
		<td>Metro latency from RJ to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.se_{metroCode}.latency</td>
		<td>Metro latency from SE to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sg_{metroCode}.latency</td>
		<td>Metro latency from SG to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sk_{metroCode}.latency</td>
		<td>Metro latency from SK to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sl_{metroCode}.latency</td>
		<td>Metro latency from SL to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.so_{metroCode}.latency</td>
		<td>Metro latency from SO to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sp_{metroCode}.latency</td>
		<td>Metro latency from SP to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.st_{metroCode}.latency</td>
		<td>Metro latency from ST to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sv_{metroCode}.latency</td>
		<td>Metro latency from SV to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sy_{metroCode}.latency</td>
		<td>Metro latency from SY to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.tr_{metroCode}.latency</td>
		<td>Metro latency from TR to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ty_{metroCode}.latency</td>
		<td>Metro latency from TY to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.va_{metroCode}.latency</td>
		<td>Metro latency from VA to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wa_{metroCode}.latency</td>
		<td>Metro latency from WA to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wi_{metroCode}.latency</td>
		<td>Metro latency from WI to ${metroCode} in ms</td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.zh_{metroCode}.latency</td>
		<td>Metro latency from ZH to ${metroCode} in ms</td>
	</tr>
</table>

</details>


---
### Equinix Identity UserAuthenticationEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/identity/v1/UserAuthenticationEvent.json)
#### Data Type
`equinix.identity.v1.UserAuthenticationEvent`
#### Supported Events, Metrics, and Alerts

<details>
<summary>Released</summary>

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>equinix.identity.user.activity.logged_in</td>
		<td>User loggedin event</td>
	</tr>
</table>

</details>


---
### Equinix Network Edge ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/network_edge/v1/ChangeEvent.json)
#### Data Type
`equinix.network_edge.v1.ChangeEvent`
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
		<td>equinix.network_edge.acl.state.created</td>
		<td>Network edge acl is created</td>
	</tr>
	<tr>
		<td>equinix.network_edge.acl.state.deleted</td>
		<td>Network edge acl is deleted</td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.acl.updated</td>
		<td>Network edge acl is updated</td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.reboot.completed</td>
		<td>Network edge device reboot completed</td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.reboot.started</td>
		<td>Network edge device reboot started</td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.state.cancelled</td>
		<td>Network edge device order cancelled</td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.state.created</td>
		<td>Network edge device created</td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.state.deleted</td>
		<td>Network edge device deleted</td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.state.provisioned</td>
		<td>Network edge device is provisioned</td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.state.provisioning</td>
		<td>Network edge device is provisioning</td>
	</tr>
</table>

</details>



---
### Equinix Resource Manager ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/resource_manager/v1/ChangeEvent.json)
#### Data Type
`equinix.resource_manager.v1.ChangeEvent`
#### Supported Events, Metrics, and Alerts



<!-- CATALOG_GENERATION_END -->
