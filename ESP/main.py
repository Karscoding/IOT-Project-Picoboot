from boot import connection
from machine import Pin, ADC
from time import sleep
import config
import urequests as requests
import json

url = f"http://{config.SERVER}:{config.PORT}{config.ENDPOINT}"

# read temperature
tmp36 = Pin(34, Pin.IN)
adc = ADC(tmp36)
led = Pin(2, Pin.OUT)

prop = 1100 / 65535

    
while connection.isconnected():

    v_out = adc.read_u16() * prop

    temp = (v_out - 500) / 10
    
    print('Temp : ',temp)
    response = requests.post(url, json=temp)
    
    answer = response.json()
    
    if answer == 'On':
        led.on()
        
    elif answer == 'Off':
        led.off()
    
    sleep(5)