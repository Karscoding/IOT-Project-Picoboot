#Bestand voor op de ESP32

import sys
import config
import network
from time import sleep
from machine import Pin

connection = network.WLAN(network.STA_IF)

led = Pin(25, Pin.OUT)  # gewijzigd pinnummer
led.on()
sleep(3)
led.off()

def connect():
    if connection.isconnected():
        print("Already connected")
        led.on()
        sleep(0.5)
        led.off()
        return

    connection.active(True)
    connection.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

    retry = 0

    while not connection.isconnected():  # wait until connection is complete
        if retry == 10:  # try 10 times
            sys.exit("Could not establish connection, check your settings")
        retry += 1
        print(retry)
        sleep(1)  # check again in a sec
    # no exit, we have a connection!
    print("Connection established")

if __name__ == "__main__":
    connect()