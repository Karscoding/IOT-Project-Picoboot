#Bestand voor op de ESP32

from boot import connection
from machine import Pin, ADC
from time import sleep
import config
import urequests as requests
import socket

laptop_ip="192.168.68.72"

url = f"http://{laptop_ip}:{config.PORT}{config.ENDPOINT}"
#aurl= f'http://{laptop_ip}:{config.PORT}{config.AENDPOINT}'
gurl= f'http://{laptop_ip}:{config.PORT}{config.GETPOINT}'


try:
    sharp_sensor = Pin(33, Pin.IN)

    tmp34 = Pin(34, Pin.IN)
    adc = ADC(tmp34)
    prop = 1100 / 65535

    led = Pin(2, Pin.OUT)
    secled= Pin(32, Pin.OUT)
    greenled=Pin(14,Pin.OUT)
    restleds=Pin(25,Pin.OUT)
except:
    ""

auth = ('teamH1', 'verified')
while connection.isconnected():
    try:
        led.off()

        #Read Distance
        #distance = sharp_sensor.value()
        #print("Distance:", distance)
        
        #Read Temperature
        v_out = adc.read_u16() * prop
        temp = (v_out - 500) / 10
        
        led.on()

        lights = requests.post(gurl, json=None, auth=auth)
        temperatuur = requests.post(url, json=temp, auth=auth)
        led.off()



    #Stuurt een request naar /Input met als string "Requests"
    #Deze returned een opdracht

        opdracht=lights.json()

        if opdracht["NOOD"] == True:
            for x in range(20):
                restleds.on()
                secled.on()
                greenled.on()
                sleep(0.1)
                restleds.off()
                secled.off()
                greenled.off()
                sleep(0.1)
        else:
            if opdracht["InstructionPass"] == 'Rechts':
                greenled.on()
                secled.off()
            elif opdracht["InstructionPass"] =='Links':
                secled.on()
                greenled.off()
            elif opdracht["InstructionPass"] == 'Uit':
                secled.off()
                greenled.off()

            if opdracht["InstructionAll"] == 'Aan':
                print("alle lampen aan")
                restleds.on()
            elif opdracht["InstructionAll"] == 'Uit':
                print("alle lampen uit")
                restleds.off()

    # sleep a little until next temperature reading
        sleep(3)
    except:
        sleep(3)

