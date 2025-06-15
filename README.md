# LED MCP Controller

This project provides a server and client for controlling an LED connected to a Raspberry Pi via GPIO, including sending Morse code messages using the LED. It consists of two main components:

- **server/**: A FastAPI-based server that exposes both REST and streamable http mcp endpoints to control the LED and send Morse code.
- **mcp/**: a local mcp server that calls the REST server
