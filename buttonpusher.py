#!/usr/bin/python3
# ################
# Demo tripping a DIO when the BrightButton is pressed
# ################
from brightbutton import BrightButton
import RPi.GPIO as GPIO
import time

DEMO_PIN_PUSHER = 11
DEMO_PUSH_DUR_SECS = 3
BUTTON_PIN_LED = 10
BUTTON_PIN_PUSHBUTTON = 9


GPIO.setmode(GPIO.BCM)
GPIO.setup(DEMO_PIN_PUSHER, GPIO.OUT)

button = BrightButton(BUTTON_PIN_LED, BUTTON_PIN_PUSHBUTTON)

while True:
  button.on()
  GPIO.output(DEMO_PIN_PUSHER, GPIO.LOW)
  while True:
    if button.IsPressed():
      break
  button.off()
  GPIO.output(DEMO_PIN_PUSHER, GPIO.HIGH)
  time.sleep(DEMO_PUSH_DUR_SECS)

GPIO.cleanup()
