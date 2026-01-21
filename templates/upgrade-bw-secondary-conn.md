# Network Bandwidth monitoring and upgrade agent

## Overview
This skill sets up and activate an Equinix agent that automatically upgrades the bandwidth of the secondary connection to be same as primary connection when the primary connection usage reaches a certain threshold.

## Prerequisites
To receive alerts from your connections, you must first set up alert rules in a stream.
If you don't have one yet, start by creating a stream, attach your connection resources to it, and then configure alert rules for those resources.

## Capabilities
- Monitor real-time network event streams
- Detect bandwidth threshold alerts
- Identify connection redundant group and primary secondary connections pair
- Analyze connection utilization patterns
- Automatically upgrade connection bandwidth
- Log all actions and decisions
- Send notifications for critical events

## Follow the action step by step below:
1. Once the cloud event is received, look at the alert rule from the cloud event message.
2. Search for an existing alert rule given the alertRule uuid extracted from the cloud event message to find out if the alert rule exists.
3. Search for the existing primary connection given the subject connection uuid from the cloud event message.
4. Extract the bandwidth and redundant_group from the connection details.
5. Identify the secondary connection of the edundant_group.
6. Upgrade the bandwidth of the secondary connection with the primary connection bandwidth.


## Available Tools
This skill can use the following tools:

*   **`fabric_search_connection`**: Searches for an existing connection `.
*   **`fabric_get_stream_alert_rule_details `**: Searches for an existing alert rule.
*   **`fabric_update_connection`**: Update connection. Used to upgrade bandwidth.

## Guidelines
*   **Prioritize Clarity**: Ensure all parameters for the MCP tools are clearly identified from the user's request before making the tool call.
*   **Error Handling**: If parameters are invalid or operations fail, log errors and stop the process.
*   **Token Efficiency**: Only call the tools when all necessary information is present, avoiding unnecessary context loading.
*   **User can specify alert rule uuid
*   **User can specify connection uuid

