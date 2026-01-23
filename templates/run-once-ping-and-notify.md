# Ping FCR agent

## Overview
This definition sets up and activates an Equinix agent that initiates a PING command on a Fabric Cloud Router in order to perform a network connectivity check. 
Once the PING operation is completed, the resulting output is collected and used to generate an email notification. 
The email is then sent to the specified recipient, ensuring that the results of the connectivity test are communicated clearly and promptly.
This agent can only run once.

## Prerequisites
Connections should be in PROVISIONED state to be eligible for bandwidth upgrade.

## Capabilities
- PING command on Fabric Cloud Router
- Email notification with PING results
- Log all actions and decisions

## Follow the action step by step below:
1. Start by fetching details of the router given the uuid. Stop if router does not exist.
2. Then initiate a PING command on the Fabric Cloud Router to test network connectivity to verify that the specified destination is reachable. Use the project of the router as the input project of the ping command.
3. After the PING operation completes, capture the results of the command, including any success or failure details. 
4. Next, send an email notification to the designated email address, using the outcome of the PING command as the email body so the recipient is clearly informed of the connectivity status and any relevant diagnostic information.


## Available Tools
This skill can use the following tools:

*   **`fabric_create_router_commands`**: Initiate a PING command on a Fabric Cloud Router by UUID.
*   **`fabric_send_email_notification`**: Sends an email notification given an email address and email body.

## Guidelines
*   **Prioritize Clarity**: Ensure all parameters for the MCP tools are clearly identified from the user's request before making the tool call.
*   **Error Handling**: If parameters are invalid or operations fail, log errors and stop the process.
*   **Token Efficiency**: Only call the tools when all necessary information is present, avoiding unnecessary context loading.
*   **Required Parameters** User should specify a router uuid.
*   **Required Parameters** User should specify a source connection uuid.
*   **Required Parameters** User should specify a destination IP address to ping.
*   **Required Parameters** User should specify an email address.
