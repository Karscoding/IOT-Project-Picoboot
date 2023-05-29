from boot import connection
from machine import Pin, ADC
from time import sleep
import config
import urequests as requests

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
restleds=Pin(25,Pin.OUT)


while connection.isconnected():
    try:
        led.off()

        #Read Distance
        #distance = sharp_sensor.value()
        #print("Distance:", distance)
        
        #Read Temperature
        v_out = adc.read_u16() * prop
        temp = (v_out - 500) / 10
        print(temp)
        
        led.on()

        lights = requests.post(gurl, json=None)
        temperatuur = requests.post(url, json=temp)
        led.off()



    #Stuurt een request naar /Input met als string "Requests"
    #Deze returned een opdracht

        opdracht=lights.json()

        if opdracht[1] == 'R':
            greenled.on()
            secled.off()
        elif opdracht[1] == 'L':
            secled.on()
            greenled.off()
        elif opdracht[1] == 'P':
            secled.off()
            greenled.off()

        if opdracht[0] == 'X':
            restleds.on()
        elif opdracht[0] == 'U':
            restleds.off()
        elif opdracht[0]== 'N':
            for x in range(3):
                restleds.on()
                secled.on()
                greenled.on()
                sleep(1)
                restleds.off()
                secled.off()
                greenled.off()
        
    # sleep a little until next temperature reading
        sleep(3)
    except:
        print('fail')