import re
from logging import Logger
from led import turn_on, turn_off, init, cleanup
from morse import send_message
from fastapi import FastAPI, Request
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level="INFO",
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
)
log: Logger = logging.getLogger("main")

init()

app: FastAPI = FastAPI()

@app.get("/led-on")
def led_on():
    turn_on()

@app.get("/led-off")
def led_off():
    turn_off()

@app.get("/morse")
def morse(text: str):
    send_message(text)

@app.on_event("shutdown")
def shutdown():
    cleanup()
