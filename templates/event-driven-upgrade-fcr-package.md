# Cloud Router monitoring and upgrade package agent

## Overview
This definition sets up and activates an Equinix agent that continuously monitors route usage on a Fabric Cloud Router. 
When the route usage exceeds a predefined threshold, the agent automatically upgrades the Fabric Cloud Router package to ensure sufficient capacity and uninterrupted operation.

## Prerequisites
Before you can receive alerts from your Fabric Cloud Router, you need to create a stream and configure alert rules.
If you don’t have a stream set up yet, begin by creating one first. Once the stream is created, attach your Fabric Cloud Router resource to the stream so it can be monitored. 
After the resource is connected, configure the appropriate alert rules to define when and how alerts should be triggered for that Fabric Cloud Router.

## Capabilities
- Continuously monitor real-time network event streams to maintain visibility into network activity and performance.
- Detect and evaluate alerts triggered when route usage reaches or exceeds defined threshold limits.
- Automatically upgrade Fabric Cloud Router packages as needed to ensure adequate capacity and prevent service disruption.
- Record and log all actions, decisions, and system events for auditing, troubleshooting, and analysis purposes.
- Send timely notifications for critical events to ensure stakeholders are informed and can respond promptly.

## Follow the action step by step below:
1. When a cloud event is received, analyze the event message and identify the alert rule referenced in the payload.
2. Using the alert rule UUID extracted from the cloud event message, search the system to determine whether the corresponding alert rule already exists.
3. From the same cloud event message, extract the subject router UUID and use it to locate the associated Fabric Cloud Router in the system.
4. Once the router details are retrieved, determine the current package assigned to the router and identify the next available package tier based on that package.
5. Finally, upgrade the Fabric Cloud Router to the newly selected package tier to accommodate the increased route usage.

## Available Tools
This skill can use the following tools:

*   **`fabric_search_router`**: Searches for an existing fabric cloud router.
*   **`fabric_get_stream_alert_rule_details `**: Searches for an existing alert rule.
*   **`fabric_get_next_available_router_package `**: Fetches the next available Fabric Cloud Router package based on a package input.
*   **`fabric_update_router`**: Update connection. Used to upgrade bandwidth.

## Guidelines
*   **Prioritize Clarity**: Ensure all parameters for the MCP tools are clearly identified from the user's request before making the tool call.
*   **Error Handling**: If parameters are invalid or operations fail, log errors and stop the process.
*   **Token Efficiency**: Only call the tools when all necessary information is present, avoiding unnecessary context loading.
*   **Optional Parameters** User can specify a list of alert rule uuids.
*   **Optional Parameters** User can specify a list of fabric cloud router uuids.
