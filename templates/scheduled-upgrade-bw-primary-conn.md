# Scheduled bandwidth upgrader agent

## Overview
This skill sets up and activate an Equinix agent that upgrades the bandwidth of a connection.
This agent is triggered at 3pm every Monday and Wednesday each month.

## Prerequisites
Connections should be in PROVISIONED state to be eligible for bandwidth upgrade.

## Capabilities
- Automatically upgrade connection bandwidth
- Log all actions and decisions

## Follow the action step by step below:
1. Search for the existing connection given the connection uuid.
2. Extract the bandwidth from the connection details, and then fetch the next available tier given the bandwidth extracted from the connection details.
3. Upgrade the bandwidth of the connection given the new bandwidth.


## Available Tools
This skill can use the following tools:

*   **`fabric_search_connection`**: Searches for an existing connection `.
*   **`fabric_update_connection`**: Update connection. Used to upgrade bandwidth.
*   **`fabric_get_next_available_bandwidth_tier `**: Fetches the next available billing tier based on a bandwidth input.

## Guidelines
*   **Prioritize Clarity**: Ensure all parameters for the MCP tools are clearly identified from the user's request before making the tool call.
*   **Error Handling**: If parameters are invalid or operations fail, log errors and stop the process.
*   **Token Efficiency**: Only call the tools when all necessary information is present, avoiding unnecessary context loading.
*   **User should specify connection uuid
