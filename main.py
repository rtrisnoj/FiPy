
from machine import ADC
from machine import Pin
import time

#initiliaze massa sensor configuration (ADC)
adc = ADC()
adc.vref(3130)

P13 = adc.channel(pin='P13',attn=ADC.ATTN_11DB)
massaValue = P13.value()

#initiliaze float sensor (GPIO pull up)
p0 = Pin('P0',mode=Pin.IN, pull=Pin.PULL_UP)
floatValue = p0.value()
    #floatValue = 1 if not tripped
    #floatValue = 0 if tripped, send alarm

# initiliaze relay (GPIO)
p2 = Pin('P2',mode=Pin.OUT)
p2.value(0)
while True:
    p2.value(0)
    time.sleep(5) #wait for 5 seconds

    print("Massa value:" + str(P13.value()))
    print("Float value:" + str(p0.value()))

    p2.value(1)
    time.sleep(1755) #sleep for 30 mins
