#!/usr/bin/python3
import RPi.GPIO as GPIO
import sys
import time

DEMO_PIN_LED = 10
DEMO_PIN_BUTTON = 9
DEMO_DELAY_SECS = 2


class BrightButton(object):
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)

  def __init__(self, ledPin, buttonPin):
    self._ledPin = ledPin
    self._buttonPin = buttonPin
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  def on(self):
    GPIO.output(self._ledPin, GPIO.HIGH)

  def off(self):
    GPIO.output(self._ledPin, GPIO.LOW)

  def IsPressed(self):
    return GPIO.input(self._buttonPin) == GPIO.HIGH

def main():
  btn = BrightButton(DEMO_PIN_LED, DEMO_PIN_BUTTON)
  btn.on()
  time.sleep(DEMO_DELAY_SECS)
  while True:
    if btn.IsPressed():
      break
  btn.off()
  time.sleep(DEMO_DELAY_SECS)

if __name__ == "__main__":
  main()
  GPIO.cleanup()
  sys.exit()
