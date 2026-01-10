# Network connection packets drop monitoring and upgrade agent

## Overview
This skill sets up and activate an Equinix agent that automatically upgrades the bandwidth of a connection when there are packets drop due to traffic over bw threshold.

## Prerequisites
To receive alerts from your connections, you must first set up alert rules in a stream.
If you don't have one yet, start by creating a stream, attach your connection resources to it, and then configure alert rules for those resources.

## Capabilities
- Monitor real-time network event streams
- Detect packet drop alerts
- Analyze connection utilization patterns
- Automatically upgrade connection bandwidth
- Log all actions and decisions
- Send notifications for critical events

## Follow the action step by step below:
1. Once the cloud event is received, look at the packet drop alert rule from the cloud event message.
2. Search for an existing alert rule given the alertRule uuid extracted from the cloud event message to find out if the alert rule exist.
3. Search for the existing connection given the subject connection uuid from the cloud event message.
4. Extract the bandwidth from the connection details, and then fetch the next available tier given the bandwidth extracted from the connection details.
5. Upgrade the bandwidth of the connection given the new bandwidth.


## Available Tools
This skill can use the following tools:

*   **`equinix_fabric_search_connection`**: Searches for an existing connection `.
*   **`equinix_fabric_get_stream_alert_rule_details `**: Searches for an existing alert rule.
*   **`equinix_fabric_update_connection`**: Update connection. Used to upgrade bandwidth.
*   **`equinix_fabric_get_next_available_bandwidth_tier `**: Fetches the next available billing tier based on a bandwidth input.

## Guidelines
*   **Prioritize Clarity**: Ensure all parameters for the MCP tools are clearly identified from the user's request before making the tool call.
*   **Error Handling**: If parameters are invalid or operations fail, log errors and stop the process.
*   **Token Efficiency**: Only call the tools when all necessary information is present, avoiding unnecessary context loading.
*   **User can specify alert rule uuid
*   **User can specify connection uuid
