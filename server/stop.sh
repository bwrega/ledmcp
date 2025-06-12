#!/usr/bin/env bash

LED_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd $LED_DIR
source $LED_DIR/setenv.sh

if [ -f "$LED_PIDFILE" ]
then
  pid=`cat $LED_PIDFILE`
  if ps -p $pid > /dev/null
  then
    pkill --signal SIGINT -P $pid
    kill -s SIGKILL $pid
  else
    echo "Error: process with $pid does not exist"
  fi
  rm $LED_PIDFILE
else
  echo "Error: no pidfile"
fi
