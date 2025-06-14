# LED server

## Installation

1. edit `install.sh` file - set python command to version that you want to use in .venv
2. run `./install.sh`
3. copy `setenv.sh.template` to `setenv.sh` and edit it

## Starting/Stopping

run `./start.sh` or `./stop.sh`

## Wiring

Connect a LED via 220 Ohm resistor
to `GPIO17` pin and `GND` pin.

See pinout: https://randomnerdtutorials.com/raspberry-pi-pinout-gpios/
