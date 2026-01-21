# Network Bandwidth monitoring and upgrade agent

## Overview
This automated agent monitors Equinix Fabric connections and maintains bandwidth parity between redundant connection pairs. 
When bandwidth utilization on a primary connection reaches a configured threshold, the agent automatically upgrades the secondary connection to match the primary connection's bandwidth, ensuring consistent performance across the redundant pair.

## Prerequisites
Before deploying this agent, ensure the following resources are configured:
1.Equinix Fabric Stream: A provisioned stream to receive cloud events
2.Alert Rules: Bandwidth threshold alert rules configured for monitoring connections
If these resources are not yet configured, create a stream, attach your connection resources, and configure appropriate alert rules before activating this agent.

## Capabilities
This agent provides the following automated monitoring and remediation capabilities:
 - Real-time Event Monitoring: Continuously monitors network event streams for bandwidth alerts
 - Threshold Detection: Identifies when connections exceed configured bandwidth utilization thresholds
 - Redundancy Analysis: Automatically discovers redundant connection pairs and identifies primary/secondary relationships
 - Intelligent Bandwidth Matching: Upgrades secondary connection bandwidth to match primary connection specifications
 - Comprehensive Logging: Records all actions, decisions, and state changes for audit and troubleshooting- Monitor real-time network event streams

## Workflow
The agent follows this automated workflow when processing bandwidth alerts:
1. Alert Rule Validation
 - Receives cloud event notification containing alert metadata
 - Validates alert rule existence using fabric_get_stream_alert_rule_details
 - Confirms alert is for bandwidth threshold monitoring
2. Primary Connection Analysis
 - Extracts connection UUID from the cloud event subject field
 - Retrieves complete connection details using fabric_search_connection
 - Extracts current bandwidth allocation
 - Identifies redundant_group membership
3. Secondary Connection Discovery
 - Identify the secondary connection of the redundant_group
 - Filters by redundancy group UUID and SECONDARY priority
 - Validates secondary connection configuration
4. Bandwidth Synchronization
 - Sets secondary bandwidth to match primary connection bandwidth
 - Logs upgrade action with before/after values


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

