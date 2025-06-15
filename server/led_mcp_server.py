from mcp.server.fastmcp import FastMCP
from led import turn_on, turn_off
from morse import send_message


mcp: FastMCP = FastMCP("LED MCP Server", stateless_http=True)

@mcp.tool()
def led_on() -> str:
    """Turn on the LED."""
    turn_on()
    return "LED turned on."

@mcp.tool()
def led_off() -> str:
    """Turn off the LED."""
    turn_off()
    return "LED turned off."

@mcp.tool()
def morse(text: str) -> str:
    """Send a message in morse code using the LED."""
    send_message(text)
    return f"Sent morse message: {text}"
