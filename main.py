from boot import connection
from machine import Pin, ADC
from time import sleep
import config
import urequests as requests
import json

url = f"http://{config.SERVER}:{config.PORT}{config.ENDPOINT}"
aurl= f'http://{config.SERVER}:{config.PORT}{config.AENDPOINT}'
gurl= f'http://{config.SERVER}:{config.PORT}{config.GETPOINT}'

sharp_sensor = Pin(26, Pin.IN)

tmp34 = Pin(34, Pin.IN)
adc = ADC(tmp34)
prop = 1100 / 65535



led = Pin(2, Pin.OUT)
secled= Pin(32, Pin.OUT)
greenled=Pin(14,Pin.OUT)

while connection.isconnected():
    led.off()
    #Read Distance
    #distance = sharp_sensor.value()
    #print("Distance:", distance)
    
    #Read Temperature
    v_out = adc.read_u16() * prop
    temp = (v_out - 500) / 10
    print(temp)
    
    led.on()
    try:
        lights = requests.post(gurl, json=None)
        temperatuur = requests.post(url, json=temp)
        #afstand= requests.post(aurl, json=1)
        led.off()
    except:
        print('mislukt')
    # flash blue LED indicating temperature was sent

    antwoord=temperatuur.json()
    print(f'het gekregen antwoord is {antwoord}')

    #Stuurt een request naar /Input met als string "Requests"
    #Deze returned een opdracht
    opdracht=lights.json()
    if opdracht == 'Stuurboord':
        greenled.on()
        secled.off()
    elif opdracht == 'Bakboord':
        secled.on()
        greenled.off()
    elif opdracht == 'Uit':
        secled.off()
        greenled.off()
    
    # sleep a little until next temperature reading
    sleep(5)