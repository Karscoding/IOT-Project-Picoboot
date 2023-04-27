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
while connection.isconnected():
    sensor_value = sharp_sensor.value()
    distance =sensor_value
    print("Distance:", distance)
    
    afstand= requests.post(aurl, json=distance)
    
    # read temperature
    v_out = adc.read_u16() * prop

    temp = (v_out - 500) / 10

    print(temp)
    
    led.on()
    temperatuur = requests.post(url, json=temp)
    led.off()

    # flash blue LED indicating temperature was sent

    antwoord=temperatuur.json()
    print(f'het gekregen antwoord is {antwoord}')
    if antwoord =='BAAN':
        secled.on()
        print('temperatuur ontvangen en is boven de 20')
    else:
        print(antwoord)
        secled.off()
        
    #Stuurt een request naar /Input met als string "Requests"
    #Deze returned een opdracht
    lights = requests.post(gurl, json=None)
    opdracht=lights.json()
    if opdracht == 'Stuurboord':
        #Stuurboord lampen aan
        pass
    elif opdracht == 'Bakboord':
        #Bakboord lampen aan
        pass
    
    # sleep a little until next temperature reading
    sleep(5)
