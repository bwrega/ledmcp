#!/usr/bin/env bash

echo -n $$ > $LED_PIDFILE

while sleep 1
do
  fastapi run server.py --port $LED_PORT
done
