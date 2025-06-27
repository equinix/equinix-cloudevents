# Equinix CloudEvents

Equinix published [CloudEvent](https://cloudevents.io/) Types

Definitive "source of truth" for the Equinix Network Observability event data formats

## CloudEvents SLO

<!-- SLO_CATEGORY -->
<table>
<tr>
<th>Category Code</th><th>Reporting Interval</th><th>Reporting Latency Max</th><th>Stream Latency Max</th><th>Original Data Retention</th><th>1 Hour Aggregation Retention</th><th>1 Day Aggregation Retention</th></tr>
<tr id='purple_metric_slo'>
<td><span style='color:purple'>PURPLE_METRIC_SLO</span></td><td>PT300S</td><td>PT720S</td><td>PT60S</td><td>PT90D</td><td>PT365D</td><td>PT1095D</td></tr>
<tr id='brown_metric_slo'>
<td><span style='color:brown'>BROWN_METRIC_SLO</span></td><td>PT300S</td><td>PT390S</td><td>PT60S</td><td>PT90D</td><td>PT365D</td><td>PT1095D</td></tr>
<tr id='blue_metric_slo'>
<td><span style='color:blue'>BLUE_METRIC_SLO</span></td><td>PT300S</td><td>PT1S</td><td>PT60S</td><td>PT90D</td><td>PT365D</td><td>PT1095D</td></tr>
<tr id='purple_event_slo'>
<td><span style='color:purple'>PURPLE_EVENT_SLO</span></td><td>-</td><td>PT480S</td><td>PT60S</td><td>PT90D</td><td>-</td><td>-</td></tr>
<tr id='brown_event_slo'>
<td><span style='color:brown'>BROWN_EVENT_SLO</span></td><td>-</td><td>PT3S</td><td>PT60S</td><td>PT90D</td><td>-</td><td>-</td></tr>
<tr id='blue_event_slo'>
<td><span style='color:blue'>BLUE_EVENT_SLO</span></td><td>-</td><td>PT1S</td><td>PT60S</td><td>PT90D</td><td>-</td><td>-</td></tr>
<tr id='blue_alert_slo'>
<td><span style='color:blue'>BLUE_ALERT_SLO</span></td><td>-</td><td>PT1S</td><td>PT60S</td><td>PT90D</td><td>-</td><td>-</td></tr>
</table>

<!-- SLO_CATEGORY_END -->

- **Reporting Interval** 
The interval at which a given metric is collected
- **Reporting Latency Max** 
The maximum latency between the time a event or metric is collected and the time it becomes available for streaming or querying 
- **Stream Latency Max** 
The maximum latency for streaming a metric or event to the configured sink  destination via the stream subscription. If the streaming attempts fails, it will be retired until this latency threshold expries. 
- **Original Data Retention** 
The duration for which the original, unaggregated data remians available for querying
- **1 Hour Aggregation Retention*** 
The duration for which data aggregated at a 1-hour interval remains available for retrieval.
- **1 Day Aggregation Retention*** 
The duration for which data aggregated at a 1-day interval remains available for retrieval.



## CloudEvents in this repository

The following data payloads are the supported events and formats for Equinix Network Observability

<!-- CATALOG_GENERATION_START -->
---
### Equinix Access Manager RoleAssignmentEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/access_manager/v1/RoleAssignmentEvent.json)
#### Data Type
`equinix.access_manager.v1.RoleAssignmentEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.access_manager.user.role.added</td>
		<td>Role assignment event</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.access_manager.user.role.removed</td>
		<td>Role unassignment event</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
</table>



---
### Equinix Fabric ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/ChangeEvent.json)
#### Data Type
`equinix.fabric.v1.ChangeEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.fabric.connection.attribute.changed</td>
		<td>Connection named ${connection_name} attributes are changed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.deprovisioned</td>
		<td>Connection named ${connection_name} state changed to deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.deprovisioning</td>
		<td>Connection named ${connection_name} state changed to deprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.failed</td>
		<td>Connection named ${connection_name} state changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.pending</td>
		<td>Connection named ${connection_name} state changed to pending</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.provisioned</td>
		<td>Connection named ${connection_name} state changed to provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.provisioning</td>
		<td>Connection named ${connection_name} state changed to provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.state.reprovisioning</td>
		<td>Connection named ${connection_name} state changed to reprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.status.down</td>
		<td>Connection '${connection_name}' status changed to DOWN</td>
		<td>released</td>
	<td><a href='#purple_event_slo'> <span style='color:purple'>PURPLE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.status.up</td>
		<td>Connection '${connection_name}' status changed to UP</td>
		<td>released</td>
	<td><a href='#purple_event_slo'> <span style='color:purple'>PURPLE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv4_session.status.active</td>
		<td>Neighbor ${IP} address session state changed to Active</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv4_session.status.connect</td>
		<td>Neighbor ${IP} address session state changed to Connect</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv4_session.status.established</td>
		<td>Neighbor ${IP} address session state changed to Established</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv4_session.status.idle</td>
		<td>Neighbor ${IP} address session state changed to Idle</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv4_session.status.open_confirm</td>
		<td>Neighbor ${IP} address session state changed to Open_confirm</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv4_session.status.open_sent</td>
		<td>Neighbor ${IP} address session state changed to Open_sent</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv6_session.status.active</td>
		<td>Neighbor ${IP} address session state changed to Active</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv6_session.status.connect</td>
		<td>Neighbor ${IP} address session state changed to Connect</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv6_session.status.established</td>
		<td>Neighbor ${IP} address session state changed to Established</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv6_session.status.idle</td>
		<td>Neighbor ${IP} address session state changed to Idle</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv6_session.status.open_confirm</td>
		<td>Neighbor ${IP} address session state changed to Open_confirm</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_bgpipv6_session.status.open_sent</td>
		<td>Neighbor ${IP} address session state changed to open_sent</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_aggregation.state.attached</td>
		<td>Connection Route Aggregation named ${route_aggregation_rule_name} attachment status changed to attached</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_aggregation.state.attaching</td>
		<td>Connection Route Aggregation named ${route_aggregation_rule_name} attachment status changed to attaching</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_aggregation.state.detached</td>
		<td>Connection Route Aggregation named ${route_aggregation_rule_name} attachment status changed to detached</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_aggregation.state.detaching</td>
		<td>Connection Route Aggregation named ${route_aggregation_rule_name} attachment status changed to detaching</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_aggregation.state.failed</td>
		<td>Connection Route Aggregation named ${route_aggregation_rule_name} attachment status changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_aggregation.state.pending_bgp_configuration</td>
		<td>Connection Route Aggregation named ${route_aggregation_rule_name} attachment status changed to pending_bgp_configuration</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_filter.state.attached</td>
		<td>Connection Route Filter named ${route_filter_rule_name} attachment status changed to attached</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_filter.state.attaching</td>
		<td>Connection Route Filter named ${route_filter_rule_name} attachment status changed to attaching</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_filter.state.detached</td>
		<td>Connection Route Filter named ${route_filter_rule_name} attachment status changed to detached</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_filter.state.detaching</td>
		<td>Connection Route Filter named ${route_filter_rule_name} attachment status changed to detaching</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_filter.state.failed</td>
		<td>Connection Route Filter named ${route_filter_rule_name} attachment status changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_route_filter.state.pending_bgp_configuration</td>
		<td>Connection Route Filter named ${route_filter_rule_name} attachment status changed to pending_bgp_configuration</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_routing_protocol.state.deprovisioned</td>
		<td>Routing Protocol named ${routing_protocol_name} state changed to deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_routing_protocol.state.deprovisioning</td>
		<td>Routing Protocol named ${routing_protocol_name} state changed to deprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_routing_protocol.state.failed</td>
		<td>Routing Protocol named ${routing_protocol_name} state changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_routing_protocol.state.provisioned</td>
		<td>Routing Protocol named ${routing_protocol_name} state changed to provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_routing_protocol.state.provisioning</td>
		<td>Routing Protocol named ${routing_protocol_name} state changed to provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection_routing_protocol.state.reprovisioning</td>
		<td>Routing Protocol named ${routing_protocol_name} state changed to reprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.internet_access.attribute.changed</td>
		<td>Internet access service changed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.internet_access.attribute.changing</td>
		<td>Internet access service changing</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.internet_access.attribute.failed</td>
		<td>Internet access service changed failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.internet_access.state.deprovisioned</td>
		<td>Internet access service de-provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.internet_access.state.deprovisioning</td>
		<td>Internet access service de-provisioning started</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.internet_access.state.failed</td>
		<td>Internet access service provisioning or de-provisioning failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.internet_access.state.provisioned</td>
		<td>Internet access service provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.internet_access.state.provisioning</td>
		<td>Internet access service provisioning started</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.network.attribute.changed</td>
		<td>network named ${network_name} attribute changed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.deprovisioned</td>
		<td>Network named ${network_name} state changed to deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.deprovisioning</td>
		<td>Network named ${network_name} state changed to deprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.provisioned</td>
		<td>Network named ${network_name} state changed to provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.network.state.provisioning</td>
		<td>Network named ${network_name} state changed to provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.physical_port.state.deprovisioned</td>
		<td>Physical port ${port_id} state changed to deprovisioned</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.physical_port.state.deprovisioning</td>
		<td>Physical port ${port_id} state changed to deprovisioning</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.physical_port.state.failed</td>
		<td>Physical port ${port_id} state changed to failed</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.physical_port.state.pending_cross_connect</td>
		<td>Physical port ${port_id} state changed to pending_cross_connect</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.physical_port.state.provisioned</td>
		<td>Physical port ${port_id} state changed to provisioned</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.physical_port.state.provisioning</td>
		<td>Physical port ${port_id} state changed to provisioning</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.deprovisioned</td>
		<td>Virtual port named ${port_name} state changed to deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.deprovisioning</td>
		<td>Virtual port named ${port_name} state changed to deprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.failed</td>
		<td>Virtual port named ${port_name} state changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.inactive</td>
		<td>Virtual port named ${port_name} state changed to inactive</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.provisioned</td>
		<td>Virtual port named ${port_name} state changed to provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.state.provisioning</td>
		<td>Virtual port named ${port_name} state changed to provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.status.down</td>
		<td>Virtual|Physical port '${port_name}' status changed to DOWN</td>
		<td>released</td>
	<td><a href='#purple_event_slo'> <span style='color:purple'>PURPLE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.status.inactive</td>
		<td>Virtual|Physical port '${port_name}' status changed to INACTIVE</td>
		<td>released</td>
	<td><a href='#purple_event_slo'> <span style='color:purple'>PURPLE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.status.up</td>
		<td>Virtual|Physical port '${port_name}' status changed to UP</td>
		<td>released</td>
	<td><a href='#purple_event_slo'> <span style='color:purple'>PURPLE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation.attribute.changed</td>
		<td>Route Aggregation named ${route_aggregation_name} attribute changed</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation.state.deprovisioned</td>
		<td>Route Aggregation named ${route_aggregation_name} state changed to deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation.state.deprovisioning</td>
		<td>Route Aggregation named ${route_aggregation_name} state changed to deprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation.state.not_deprovisioned</td>
		<td>Route Aggregation named ${route_aggregation_name} state changed to not_deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation.state.not_provisioned</td>
		<td>Route Aggregation named ${route_aggregation_name} state changed to not_provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation.state.provisioned</td>
		<td>Route Aggregation named ${route_aggregation_name} state changed to provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation.state.provisioning</td>
		<td>Route Aggregation named ${route_aggregation_name} state changed to provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation.state.reprovisioning</td>
		<td>Route Aggregation named ${route_aggregation_name} state changed to reprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation_rule.attribute.changed</td>
		<td>Route Aggregation Rule named ${route_aggregation_rule_name} attribute changed</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation_rule.state.deprovisioned</td>
		<td>Route Aggregation Rule named ${route_aggregation_rule_name} state changed to deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation_rule.state.deprovisioning</td>
		<td>Route Aggregation Rule named ${route_aggregation_rule_name} state changed to deprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation_rule.state.failed</td>
		<td>Route Aggregation Rule named ${route_aggregation_rule_name} state changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation_rule.state.provisioned</td>
		<td>Route Aggregation Rule named ${route_aggregation_rule_name} state changed to provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation_rule.state.provisioning</td>
		<td>Route Aggregation Rule named ${route_aggregation_rule_name} state changed to provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_aggregation_rule.state.reprovisioning</td>
		<td>Route Aggregation Rule named ${route_aggregation_rule_name} state changed to reprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter.attribute.changed</td>
		<td>Route Filter named ${route_filter_name} attribute changed</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter.state.deprovisioned</td>
		<td>Route Filter named ${route_filter_name} state changed to deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter.state.deprovisioning</td>
		<td>Route Filter named ${route_filter_name} state changed to deprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter.state.not_deprovisioned</td>
		<td>Route Filter named ${route_filter_name} state changed to not_deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter.state.not_provisioned</td>
		<td>Route Filter named ${route_filter_name} state changed to not_provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter.state.provisioned</td>
		<td>Route Filter named ${route_filter_name} state changed to provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter.state.provisioning</td>
		<td>Route Filter named ${route_filter_name} state changed to provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter.state.reprovisioning</td>
		<td>Route Filter named ${route_filter_name} state changed to reprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter_rule.attribute.changed</td>
		<td>Route Filter Rule named ${route_filter_rule_name} attribute changed</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter_rule.state.deprovisioned</td>
		<td>Route Filter Rule named ${route_filter_rule_name} state changed to deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter_rule.state.deprovisioning</td>
		<td>Route Filter Rule named ${route_filter_rule_name} state changed to deprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter_rule.state.failed</td>
		<td>Route Filter Rule named ${route_filter_rule_name} state changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter_rule.state.provisioned</td>
		<td>Route Filter Rule named ${route_filter_rule_name} state changed to provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter_rule.state.provisioning</td>
		<td>Route Filter Rule named ${route_filter_rule_name} state changed to provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.route_filter_rule.state.reprovisioning</td>
		<td>Route Filter Rule named ${route_filter_rule_name} state changed to reprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.attribute.changed</td>
		<td>Router named ${router_name} attribute changed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.deprovisioned</td>
		<td>Router named ${router_name} successfully deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.deprovisioning</td>
		<td>Router named ${router_name} state changed to deprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.failed</td>
		<td>Router named ${router_name} state changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.not_deprovisioned</td>
		<td>Router named ${router_name} state changed to not_deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.not_provisioned</td>
		<td>Router named ${router_name} state changed to not_provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.provisioned</td>
		<td>Router named ${router_name} successfully provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.provisioning</td>
		<td>Router named ${router_name} state changed to provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.state.reprovisioning</td>
		<td>Router named ${router_name} state changed to reprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router_action.state.failed</td>
		<td>Router Action state changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router_action.state.pending</td>
		<td>Router Action state changed to pending</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router_action.state.succeeded</td>
		<td>Router Action state changed to succeeded</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router_command.state.deleted</td>
		<td>Router Command state changed to deleted</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router_command.state.failed</td>
		<td>Router Command state changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router_command.state.pending</td>
		<td>Router Command state changed to pending</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router_command.state.succeeded</td>
		<td>Router Command state changed to succeeded</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.routing_protocol_action.state.failed</td>
		<td>Routing Protocol Action state changed to failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.routing_protocol_action.state.pending</td>
		<td>Routing Protocol Action state changed to pending</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.routing_protocol_action.state.succeeded</td>
		<td>Routing Protocol Action state changed to succeeded</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.attribute.changed</td>
		<td>Token successfully updated</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.resend_email_notification.failed</td>
		<td>Token resend email notification failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.resend_email_notification.succeeded</td>
		<td>Token resend email notification succeeded</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.state.active</td>
		<td>Token successfully activated</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.state.deleted</td>
		<td>Token successfully deleted</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.state.expired</td>
		<td>Token expired</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.service_token.state.inactive</td>
		<td>Token successfully deactivated</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
</table>



---
### Equinix Fabric MetricAlert
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/MetricAlert.json)
#### Data Type
`equinix.fabric.v1.MetricAlert`
#### Supported Events, Metrics, and Alerts


#### Alerts

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bandwidth_rx.usage</td>
		<td>Connection inbound bandwidth usage is ${operator} ${operand} bit/s</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bandwidth_tx.usage</td>
		<td>Connection outbound bandwidth usage is ${operator} ${operand} bit/s</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.installed_routes_ipv4.utilization</td>
		<td>Utilization of connection active IPv4 routes is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.installed_routes_ipv6.utilization</td>
		<td>Utilization of connection active IPv6 routes is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.packets_dropped_rx_aside_rateexceeded.count</td>
		<td>Connection A side inbound dropped packets count is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.packets_dropped_rx_zside_rateexceeded.count</td>
		<td>Connection Z side inbound dropped packets count is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.packets_dropped_tx_aside_rateexceeded.count</td>
		<td>Connection A side outbound dropped packets count is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.packets_dropped_tx_zside_rateexceeded.count</td>
		<td>Connection Z side outbound dropped packets count is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.am_{metroCode}.latency</td>
		<td>Metro latency from Amsterdam to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.at_{metroCode}.latency</td>
		<td>Metro latency from Atlanta to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ba_{metroCode}.latency</td>
		<td>Metro latency from Barcelona to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bg_{metroCode}.latency</td>
		<td>Metro latency from Bogota to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bl_{metroCode}.latency</td>
		<td>Metro latency from Brussels to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bo_{metroCode}.latency</td>
		<td>Metro latency from Boston to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bx_{metroCode}.latency</td>
		<td>Metro latency from Bordeaux to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ca_{metroCode}.latency</td>
		<td>Metro latency from Canberra to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ch_{metroCode}.latency</td>
		<td>Metro latency from Chicago to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cl_{metroCode}.latency</td>
		<td>Metro latency from Calgary to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cu_{metroCode}.latency</td>
		<td>Metro latency from Culpeper to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.da_{metroCode}.latency</td>
		<td>Metro latency from Dallas to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.db_{metroCode}.latency</td>
		<td>Metro latency from Dublin to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dc_{metroCode}.latency</td>
		<td>Metro latency from Ashburn to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.de_{metroCode}.latency</td>
		<td>Metro latency from Denver to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dx_{metroCode}.latency</td>
		<td>Metro latency from Dubai to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.fr_{metroCode}.latency</td>
		<td>Metro latency from Frankfurt to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.gv_{metroCode}.latency</td>
		<td>Metro latency from Geneva to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.he_{metroCode}.latency</td>
		<td>Metro latency from Helsinki to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hh_{metroCode}.latency</td>
		<td>Metro latency from Hamburg to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hk_{metroCode}.latency</td>
		<td>Metro latency from Hong Kong to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ho_{metroCode}.latency</td>
		<td>Metro latency from Houston to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.il_{metroCode}.latency</td>
		<td>Metro latency from Istanbul to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jh_{metroCode}.latency</td>
		<td>Metro latency from Johor to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jk_{metroCode}.latency</td>
		<td>Metro latency from Jakarta to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jn_{metroCode}.latency</td>
		<td>Metro latency from Johannesburg to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ka_{metroCode}.latency</td>
		<td>Metro latency from Kamloops to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.kl_{metroCode}.latency</td>
		<td>Metro latency from Kuala Lumpur to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.la_{metroCode}.latency</td>
		<td>Metro latency from Los Angeles to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ld_{metroCode}.latency</td>
		<td>Metro latency from London to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.lm_{metroCode}.latency</td>
		<td>Metro latency from Lima to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ls_{metroCode}.latency</td>
		<td>Metro latency from Lisbon to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ma_{metroCode}.latency</td>
		<td>Metro latency from Manchester to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mb_{metroCode}.latency</td>
		<td>Metro latency from Mumbai to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.md_{metroCode}.latency</td>
		<td>Metro latency from Madrid to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.me_{metroCode}.latency</td>
		<td>Metro latency from Melbourne to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mi_{metroCode}.latency</td>
		<td>Metro latency from Miami to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ml_{metroCode}.latency</td>
		<td>Metro latency from Milan to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mo_{metroCode}.latency</td>
		<td>Metro latency from Monterrey to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mt_{metroCode}.latency</td>
		<td>Metro latency from Montreal to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mu_{metroCode}.latency</td>
		<td>Metro latency from Munich to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mx_{metroCode}.latency</td>
		<td>Metro latency from Mexico City to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ny_{metroCode}.latency</td>
		<td>Metro latency from New York to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.os_{metroCode}.latency</td>
		<td>Metro latency from Osaka to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ot_{metroCode}.latency</td>
		<td>Metro latency from Ottawa to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pa_{metroCode}.latency</td>
		<td>Metro latency from Paris to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pe_{metroCode}.latency</td>
		<td>Metro latency from Perth to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ph_{metroCode}.latency</td>
		<td>Metro latency from Philadelphia to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.rj_{metroCode}.latency</td>
		<td>Metro latency from Rio de Janeiro to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.se_{metroCode}.latency</td>
		<td>Metro latency from Seattle to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sg_{metroCode}.latency</td>
		<td>Metro latency from Singapore to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sk_{metroCode}.latency</td>
		<td>Metro latency from Stockholm to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sl_{metroCode}.latency</td>
		<td>Metro latency from Seoul to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.so_{metroCode}.latency</td>
		<td>Metro latency from Sofia to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sp_{metroCode}.latency</td>
		<td>Metro latency from Sao Paulo to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.st_{metroCode}.latency</td>
		<td>Metro latency from Santiago to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sv_{metroCode}.latency</td>
		<td>Metro latency from Silicon Valley to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sy_{metroCode}.latency</td>
		<td>Metro latency from Sydney to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.tr_{metroCode}.latency</td>
		<td>Metro latency from Toronto to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ty_{metroCode}.latency</td>
		<td>Metro latency from Tokyo to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.va_{metroCode}.latency</td>
		<td>Metro latency from Vancouver to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wa_{metroCode}.latency</td>
		<td>Metro latency from Warsaw to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wi_{metroCode}.latency</td>
		<td>Metro latency from Winnipeg to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.zh_{metroCode}.latency</td>
		<td>Metro latency from Zurich to ${metro} is ${operator} ${operand} milliseconds</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.bandwidth_rx.usage</td>
		<td>Port inbound bandwidth usage is ${operator} ${operand} bit/s</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.bandwidth_tx.usage</td>
		<td>Port outbound bandwidth usage is ${operator} ${operand} bit/s</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_dropped_rx.count</td>
		<td>Port inbound dropped packets count is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_dropped_tx.count</td>
		<td>Port outbound dropped packets count is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_erred_rx.count</td>
		<td>Port inbound erred packets count is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_erred_tx.count</td>
		<td>Port outbound erred packets count is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.installed_routes_ipv4.utilization</td>
		<td>Utilization of router total IPv4 routes is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.router.installed_routes_ipv6.utilization</td>
		<td>Utilization of router total IPv6 routes is ${operator} ${operand}</td>
		<td>released</td>
	<td><a href='#brown_event_slo'> <span style='color:brown'>BROWN_EVENT_SLO</span></a></td>
	</tr>
</table>

---
### Equinix Fabric MetricEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/MetricEvent.json)
#### Data Type
`equinix.fabric.v1.MetricEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.fabric.metric</td>
		<td>Metrics collected</td>
		<td>released</td>
	<td>-</td>
	</tr>
</table>

#### Metrics

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bandwidth_rx.usage</td>
		<td>Connection inbound bandwidth usage in bit/sec</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.bandwidth_tx.usage</td>
		<td>Connection outbound bandwidth usage in bit/sec</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.packets_dropped_rx_aside_rateexceeded.count</td>
		<td>Connection A side inbound dropped packets count</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.packets_dropped_rx_zside_rateexceeded.count</td>
		<td>Connection Z side inbound dropped packets count</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.packets_dropped_tx_aside_rateexceeded.count</td>
		<td>Connection A side outbound dropped packets count</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.connection.packets_dropped_tx_zside_rateexceeded.count</td>
		<td>Connection Z side outbound dropped packets count</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.am_{metroCode}.latency</td>
		<td>Amsterdam to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.at_{metroCode}.latency</td>
		<td>Atlanta to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ba_{metroCode}.latency</td>
		<td>Barcelona to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bg_{metroCode}.latency</td>
		<td>Bogota to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bl_{metroCode}.latency</td>
		<td>Brussels to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bo_{metroCode}.latency</td>
		<td>Boston to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bx_{metroCode}.latency</td>
		<td>Bordeaux to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ca_{metroCode}.latency</td>
		<td>Canberra to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ch_{metroCode}.latency</td>
		<td>Chicago to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cl_{metroCode}.latency</td>
		<td>Calgary to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cu_{metroCode}.latency</td>
		<td>Culpeper to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.da_{metroCode}.latency</td>
		<td>Dallas to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.db_{metroCode}.latency</td>
		<td>Dublin to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dc_{metroCode}.latency</td>
		<td>Ashburn to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.de_{metroCode}.latency</td>
		<td>Denver to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dx_{metroCode}.latency</td>
		<td>Dubai to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.fr_{metroCode}.latency</td>
		<td>Frankfurt to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.gv_{metroCode}.latency</td>
		<td>Geneva to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.he_{metroCode}.latency</td>
		<td>Helsinki to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hh_{metroCode}.latency</td>
		<td>Hamburg to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hk_{metroCode}.latency</td>
		<td>Hong Kong to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ho_{metroCode}.latency</td>
		<td>Houston to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.il_{metroCode}.latency</td>
		<td>Istanbul to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jh_{metroCode}.latency</td>
		<td>Johor to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jk_{metroCode}.latency</td>
		<td>Jakarta to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jn_{metroCode}.latency</td>
		<td>Johannesburg to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ka_{metroCode}.latency</td>
		<td>Kamloops to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.kl_{metroCode}.latency</td>
		<td>Kuala Lumpur to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.la_{metroCode}.latency</td>
		<td>Los Angeles to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ld_{metroCode}.latency</td>
		<td>London to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.lm_{metroCode}.latency</td>
		<td>Lima to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ls_{metroCode}.latency</td>
		<td>Lisbon to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ma_{metroCode}.latency</td>
		<td>Manchester to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mb_{metroCode}.latency</td>
		<td>Mumbai to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.md_{metroCode}.latency</td>
		<td>Madrid to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.me_{metroCode}.latency</td>
		<td>Melbourne to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mi_{metroCode}.latency</td>
		<td>Miami to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ml_{metroCode}.latency</td>
		<td>Milan to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mo_{metroCode}.latency</td>
		<td>Monterrey to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mt_{metroCode}.latency</td>
		<td>Montreal to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mu_{metroCode}.latency</td>
		<td>Munich to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mx_{metroCode}.latency</td>
		<td>Mexico City to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ny_{metroCode}.latency</td>
		<td>New York to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.os_{metroCode}.latency</td>
		<td>Osaka to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ot_{metroCode}.latency</td>
		<td>Ottawa to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pa_{metroCode}.latency</td>
		<td>Paris to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pe_{metroCode}.latency</td>
		<td>Perth to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ph_{metroCode}.latency</td>
		<td>Philadelphia to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.rj_{metroCode}.latency</td>
		<td>Rio de Janeiro to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.se_{metroCode}.latency</td>
		<td>Seattle to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sg_{metroCode}.latency</td>
		<td>Singapore to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sk_{metroCode}.latency</td>
		<td>Stockholm to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sl_{metroCode}.latency</td>
		<td>Seoul to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.so_{metroCode}.latency</td>
		<td>Sofia to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sp_{metroCode}.latency</td>
		<td>Sao Paulo to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.st_{metroCode}.latency</td>
		<td>Santiago to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sv_{metroCode}.latency</td>
		<td>Silicon Valley to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sy_{metroCode}.latency</td>
		<td>Sydney to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.tr_{metroCode}.latency</td>
		<td>Toronto to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ty_{metroCode}.latency</td>
		<td>Tokyo to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.va_{metroCode}.latency</td>
		<td>Vancouver to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wa_{metroCode}.latency</td>
		<td>Warsaw to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wi_{metroCode}.latency</td>
		<td>Winnipeg to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.zh_{metroCode}.latency</td>
		<td>Zurich to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.bandwidth_rx.usage</td>
		<td>Port inbound bandwidth usage in bit/sec</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.bandwidth_tx.usage</td>
		<td>Port outbound bandwidth usage in bit/sec</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_dropped_rx.count</td>
		<td>Port inbound dropped packets count</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_dropped_tx.count</td>
		<td>Port outbound dropped packets count</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_erred_rx.count</td>
		<td>Port inbound erred packets count</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.port.packets_erred_tx.count</td>
		<td>Port outbound erred packets count</td>
		<td>released</td>
	<td><a href='#purple_metric_slo'> <span style='color:purple'>PURPLE_METRIC_SLO</span></a></td>
	</tr>
</table>


---
### Equinix Fabric Metro Latency Alert (Deprecated)
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/MetroLatencyAlert.json)
#### Data Type
`equinix.fabric.v1.MetroLatencyAlert`
#### Supported Events, Metrics, and Alerts


#### Alerts

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.fabric.metro.am_{metroCode}.latency</td>
		<td>Metro latency from Amsterdam to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.at_{metroCode}.latency</td>
		<td>Metro latency from Atlanta to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ba_{metroCode}.latency</td>
		<td>Metro latency from Barcelona to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bg_{metroCode}.latency</td>
		<td>Metro latency from Bogota to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bl_{metroCode}.latency</td>
		<td>Metro latency from Brussels to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bo_{metroCode}.latency</td>
		<td>Metro latency from Boston to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bx_{metroCode}.latency</td>
		<td>Metro latency from Bordeaux to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ca_{metroCode}.latency</td>
		<td>Metro latency from Canberra to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ch_{metroCode}.latency</td>
		<td>Metro latency from Chicago to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cl_{metroCode}.latency</td>
		<td>Metro latency from Calgary to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cu_{metroCode}.latency</td>
		<td>Metro latency from Culpeper to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.da_{metroCode}.latency</td>
		<td>Metro latency from Dallas to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.db_{metroCode}.latency</td>
		<td>Metro latency from Dublin to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dc_{metroCode}.latency</td>
		<td>Metro latency from Ashburn to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.de_{metroCode}.latency</td>
		<td>Metro latency from Denver to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dx_{metroCode}.latency</td>
		<td>Metro latency from Dubai to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.fr_{metroCode}.latency</td>
		<td>Metro latency from Frankfurt to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.gv_{metroCode}.latency</td>
		<td>Metro latency from Geneva to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.he_{metroCode}.latency</td>
		<td>Metro latency from Helsinki to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hh_{metroCode}.latency</td>
		<td>Metro latency from Hamburg to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hk_{metroCode}.latency</td>
		<td>Metro latency from Hong Kong to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ho_{metroCode}.latency</td>
		<td>Metro latency from Houston to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.il_{metroCode}.latency</td>
		<td>Metro latency from Istanbul to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jh_{metroCode}.latency</td>
		<td>Metro latency from Johor to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jk_{metroCode}.latency</td>
		<td>Metro latency from Jakarta to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jn_{metroCode}.latency</td>
		<td>Metro latency from Johannesburg to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ka_{metroCode}.latency</td>
		<td>Metro latency from Kamloops to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.kl_{metroCode}.latency</td>
		<td>Metro latency from Kuala Lumpur to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.la_{metroCode}.latency</td>
		<td>Metro latency from Los Angeles to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ld_{metroCode}.latency</td>
		<td>Metro latency from London to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.lm_{metroCode}.latency</td>
		<td>Metro latency from Lima to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ls_{metroCode}.latency</td>
		<td>Metro latency from Lisbon to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ma_{metroCode}.latency</td>
		<td>Metro latency from Manchester to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mb_{metroCode}.latency</td>
		<td>Metro latency from Mumbai to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.md_{metroCode}.latency</td>
		<td>Metro latency from Madrid to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.me_{metroCode}.latency</td>
		<td>Metro latency from Melbourne to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mi_{metroCode}.latency</td>
		<td>Metro latency from Miami to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ml_{metroCode}.latency</td>
		<td>Metro latency from Milan to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mo_{metroCode}.latency</td>
		<td>Metro latency from Monterrey to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mt_{metroCode}.latency</td>
		<td>Metro latency from Montreal to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mu_{metroCode}.latency</td>
		<td>Metro latency from Munich to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mx_{metroCode}.latency</td>
		<td>Metro latency from Mexico City to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ny_{metroCode}.latency</td>
		<td>Metro latency from New York to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.os_{metroCode}.latency</td>
		<td>Metro latency from Osaka to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ot_{metroCode}.latency</td>
		<td>Metro latency from Ottawa to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pa_{metroCode}.latency</td>
		<td>Metro latency from Paris to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pe_{metroCode}.latency</td>
		<td>Metro latency from Perth to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ph_{metroCode}.latency</td>
		<td>Metro latency from Philadelphia to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.rj_{metroCode}.latency</td>
		<td>Metro latency from Rio de Janeiro to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.se_{metroCode}.latency</td>
		<td>Metro latency from Seattle to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sg_{metroCode}.latency</td>
		<td>Metro latency from Singapore to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sk_{metroCode}.latency</td>
		<td>Metro latency from Stockholm to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sl_{metroCode}.latency</td>
		<td>Metro latency from Seoul to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.so_{metroCode}.latency</td>
		<td>Metro latency from Sofia to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sp_{metroCode}.latency</td>
		<td>Metro latency from Sao Paulo to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.st_{metroCode}.latency</td>
		<td>Metro latency from Santiago to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sv_{metroCode}.latency</td>
		<td>Metro latency from Silicon Valley to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sy_{metroCode}.latency</td>
		<td>Metro latency from Sydney to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.tr_{metroCode}.latency</td>
		<td>Metro latency from Toronto to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ty_{metroCode}.latency</td>
		<td>Metro latency from Tokyo to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.va_{metroCode}.latency</td>
		<td>Metro latency from Vancouver to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wa_{metroCode}.latency</td>
		<td>Metro latency from Warsaw to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wi_{metroCode}.latency</td>
		<td>Metro latency from Winnipeg to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.zh_{metroCode}.latency</td>
		<td>Metro latency from Zurich to ${metro} above ${threshold}</td>
		<td>released</td>
	<td><a href='#blue_alert_slo'> <span style='color:blue'>BLUE_ALERT_SLO</span></a></td>
	</tr>
</table>

---
### Equinix Fabric Metro Latency Metric (Deprecated)
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/fabric/v1/MetroLatencyMetric.json)
#### Data Type
`equinix.fabric.v1.MetroLatencyMetric`
#### Supported Events, Metrics, and Alerts
#### Events

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.fabric.metric</td>
		<td>Metrics collected</td>
		<td>released</td>
	<td>-</td>
	</tr>
</table>

#### Metrics

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.fabric.metro.am_{metroCode}.latency</td>
		<td>Amsterdam to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.at_{metroCode}.latency</td>
		<td>Atlanta to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ba_{metroCode}.latency</td>
		<td>Barcelona to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bg_{metroCode}.latency</td>
		<td>Bogota to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bl_{metroCode}.latency</td>
		<td>Brussels to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bo_{metroCode}.latency</td>
		<td>Boston to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.bx_{metroCode}.latency</td>
		<td>Bordeaux to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ca_{metroCode}.latency</td>
		<td>Canberra to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ch_{metroCode}.latency</td>
		<td>Chicago to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cl_{metroCode}.latency</td>
		<td>Calgary to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.cu_{metroCode}.latency</td>
		<td>Culpeper to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.da_{metroCode}.latency</td>
		<td>Dallas to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.db_{metroCode}.latency</td>
		<td>Dublin to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dc_{metroCode}.latency</td>
		<td>Ashburn to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.de_{metroCode}.latency</td>
		<td>Denver to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.dx_{metroCode}.latency</td>
		<td>Dubai to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.fr_{metroCode}.latency</td>
		<td>Frankfurt to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.gv_{metroCode}.latency</td>
		<td>Geneva to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.he_{metroCode}.latency</td>
		<td>Helsinki to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hh_{metroCode}.latency</td>
		<td>Hamburg to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.hk_{metroCode}.latency</td>
		<td>Hong Kong to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ho_{metroCode}.latency</td>
		<td>Houston to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.il_{metroCode}.latency</td>
		<td>Istanbul to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jh_{metroCode}.latency</td>
		<td>Johor to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jk_{metroCode}.latency</td>
		<td>Jakarta to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.jn_{metroCode}.latency</td>
		<td>Johannesburg to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ka_{metroCode}.latency</td>
		<td>Kamloops to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.kl_{metroCode}.latency</td>
		<td>Kuala Lumpur to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.la_{metroCode}.latency</td>
		<td>Los Angeles to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ld_{metroCode}.latency</td>
		<td>London to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.lm_{metroCode}.latency</td>
		<td>Lima to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ls_{metroCode}.latency</td>
		<td>Lisbon to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ma_{metroCode}.latency</td>
		<td>Manchester to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mb_{metroCode}.latency</td>
		<td>Mumbai to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.md_{metroCode}.latency</td>
		<td>Madrid to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.me_{metroCode}.latency</td>
		<td>Melbourne to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mi_{metroCode}.latency</td>
		<td>Miami to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ml_{metroCode}.latency</td>
		<td>Milan to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mo_{metroCode}.latency</td>
		<td>Monterrey to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mt_{metroCode}.latency</td>
		<td>Montreal to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mu_{metroCode}.latency</td>
		<td>Munich to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.mx_{metroCode}.latency</td>
		<td>Mexico City to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ny_{metroCode}.latency</td>
		<td>New York to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.os_{metroCode}.latency</td>
		<td>Osaka to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ot_{metroCode}.latency</td>
		<td>Ottawa to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pa_{metroCode}.latency</td>
		<td>Paris to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.pe_{metroCode}.latency</td>
		<td>Perth to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ph_{metroCode}.latency</td>
		<td>Philadelphia to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.rj_{metroCode}.latency</td>
		<td>Rio de Janeiro to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.se_{metroCode}.latency</td>
		<td>Seattle to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sg_{metroCode}.latency</td>
		<td>Singapore to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sk_{metroCode}.latency</td>
		<td>Stockholm to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sl_{metroCode}.latency</td>
		<td>Seoul to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.so_{metroCode}.latency</td>
		<td>Sofia to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sp_{metroCode}.latency</td>
		<td>Sao Paulo to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.st_{metroCode}.latency</td>
		<td>Santiago to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sv_{metroCode}.latency</td>
		<td>Silicon Valley to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.sy_{metroCode}.latency</td>
		<td>Sydney to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.tr_{metroCode}.latency</td>
		<td>Toronto to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.ty_{metroCode}.latency</td>
		<td>Tokyo to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.va_{metroCode}.latency</td>
		<td>Vancouver to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wa_{metroCode}.latency</td>
		<td>Warsaw to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.wi_{metroCode}.latency</td>
		<td>Winnipeg to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.metro.zh_{metroCode}.latency</td>
		<td>Zurich to ${metro} intermetro latency, average in milliseconds</td>
		<td>released</td>
	<td><a href='#brown_metric_slo'> <span style='color:brown'>BROWN_METRIC_SLO</span></a></td>
	</tr>
</table>


---
### Equinix Identity UserAuthenticationEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/identity/v1/UserAuthenticationEvent.json)
#### Data Type
`equinix.identity.v1.UserAuthenticationEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.identity.user.activity.logged_in</td>
		<td>User loggedIn event</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.identity.user.activity.logged_out</td>
		<td>User loggedOut event</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
</table>



---
### Equinix Identity UserEmailChangedEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/identity/v1/UserEmailChangedEvent.json)
#### Data Type
`equinix.identity.v1.UserEmailChangedEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.identity.user.email.changed</td>
		<td>User changed email address</td>
		<td>preview</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
</table>



---
### Equinix Identity UserOrgLinkageEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/identity/v1/UserOrgLinkageEvent.json)
#### Data Type
`equinix.identity.v1.UserOrgLinkageEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.identity.organization.user.added</td>
		<td>User added to org event</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.identity.organization.user.removed</td>
		<td>User removed from org event</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
</table>



---
### Equinix Network Edge ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/network_edge/v1/ChangeEvent.json)
#### Data Type
`equinix.network_edge.v1.ChangeEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.network_edge.acl.state.created</td>
		<td>Network edge acl is created</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.acl.state.deleted</td>
		<td>Network edge acl is deleted</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.acl.updated</td>
		<td>Network edge acl is updated</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.attribute.changed</td>
		<td>Network edge device attributes updated</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.reboot.completed</td>
		<td>Network edge device reboot completed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.reboot.started</td>
		<td>Network edge device reboot started</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.state.cancelled</td>
		<td>Network edge device order cancelled</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.state.created</td>
		<td>Network edge device created</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.state.deleted</td>
		<td>Network edge device deleted</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.state.provisioned</td>
		<td>Network edge device is provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.device.state.provisioning</td>
		<td>Network edge device is provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.devicelinkgroup.state.created</td>
		<td>Network edge device link group is created</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.devicelinkgroup.state.deleted</td>
		<td>Network edge device link group is deleted</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.network_edge.devicelinkgroup.state.updated</td>
		<td>Network edge device link group is updated</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
</table>



---
### Equinix Resource Manager ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/resource_manager/v1/ChangeEvent.json)
#### Data Type
`equinix.resource_manager.v1.ChangeEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.resource_manager.organization.state.created</td>
		<td>Organization created event.</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.resource_manager.organization.state.deleted</td>
		<td>Organization deleted event.</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.resource_manager.organization.state.updated</td>
		<td>Organization updated event.</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.resource_manager.project.state.created</td>
		<td>Project created event.</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.resource_manager.project.state.deleted</td>
		<td>Project deleted event.</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.resource_manager.project.state.updated</td>
		<td>Project updated event.</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
</table>



---
### Equinix Time Service ChangeEvent
#### DataSchema [JSON](https://equinix.github.io/equinix-cloudevents/jsonschema/equinix/time_service/v1/ChangeEvent.json)
#### Data Type
`equinix.time_service.v1.ChangeEvent`
#### Supported Events, Metrics, and Alerts
#### Events

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
		<th>Release Status</th>
		<th>SLO Category</th>
	</tr>
	<tr>
		<td>equinix.fabric.time_service.state.cancelled</td>
		<td>Time Service is cancelled</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.time_service.state.configuring</td>
		<td>Time Service is configuring</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.time_service.state.configuring_failed</td>
		<td>Time Service is configuring failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.time_service.state.deprovisioned</td>
		<td>Time Service is deprovisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.time_service.state.deprovisioning</td>
		<td>Time Service is deprovisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.time_service.state.deprovisioning_failed</td>
		<td>Time Service is deprovisioning failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.time_service.state.draft</td>
		<td>Time Service is in draft state</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.time_service.state.provisioned</td>
		<td>Time Service is provisioned</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.time_service.state.provisioning</td>
		<td>Time Service is provisioning</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
	<tr>
		<td>equinix.fabric.time_service.state.provisioning_failed</td>
		<td>Time Service is provisioning failed</td>
		<td>released</td>
	<td><a href='#blue_event_slo'> <span style='color:blue'>BLUE_EVENT_SLO</span></a></td>
	</tr>
</table>



<!-- CATALOG_GENERATION_END -->