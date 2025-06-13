import RPi.GPIO as GPIO
import time

LED_PIN = 17

def init():
    GPIO.setmode(GPIO.BCM)         # Use BCM pin numbering
    GPIO.setup(LED_PIN, GPIO.OUT)  # Set pin as output

def turn_on():
    GPIO.output(LED_PIN, GPIO.HIGH)

def turn_off():
    GPIO.output(LED_PIN, GPIO.LOW)

def cleanup():
    GPIO.cleanup()

def main():
    try:
        init()
        for _ in range(3):
            turn_on()
            time.sleep(1)
            turn_off()
            time.sleep(1)
    finally:
        cleanup()

if __name__ == "__main__":
    main()
