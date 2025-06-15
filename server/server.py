from led import turn_on, turn_off, init, cleanup
from morse import send_message
from fastapi import FastAPI
import contextlib
import led_mcp_server

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        init()
        await stack.enter_async_context(led_mcp_server.mcp)
        yield
        cleanup()

app: FastAPI = FastAPI(lifespan=lifespan)

@app.get("/led-on")
def led_on() -> None:
    turn_on()

@app.get("/led-off")
def led_off() -> None:
    turn_off()

@app.get("/morse")
def morse(text: str) -> None:
    send_message(text)

app.mount("/mcp", led_mcp_server.mcp.streamable_http_app())
