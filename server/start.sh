#!/usr/bin/env bash
LED_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd $LED_DIR
source $LED_DIR/setenv.sh

nohup ./run_loop.sh >>$LED_LOGFILE 2>&1 &
