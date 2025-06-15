from mcp.server.fastmcp import FastMCP
import requests

url_prefix = "http://pi:7777"

mcp: FastMCP = FastMCP("LED Controller")

@mcp.tool()
def turn_on_led() -> str:
    """Turns on the LED"""
    response: requests.Response = requests.get(f"{url_prefix}/led-on")
    if response.status_code == 200:
        return "LED turned on successfully"
    return f"Failed to turn on LED: {response.status_code}"

@mcp.tool()
def turn_off_led() -> str:
    """Turns off the LED"""
    response: requests.Response = requests.get(f"{url_prefix}/led-off")
    if response.status_code == 200:
        return "LED turned off successfully"
    return f"Failed to turn off LED: {response.status_code}"

@mcp.tool()
def send_morse_message(text: str) -> str:
    """Sends a message in morse code using the LED"""
    response: requests.Response = requests.get(f"{url_prefix}/morse", params={"text": text})
    if response.status_code == 200:
        return f"Sent morse message: {text}"
    return f"Failed to send morse message: {response.status_code}"

