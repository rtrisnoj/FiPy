
import machine
from machine import ADC
from machine import Pin
from network import Sigfox
from deepsleep import DeepSleep
import deepsleep
import socket
import time
import binascii
import sys

#initiliaze massa sensor configuration (ADC)
adc = ADC()
adc.vref(3130)

pin_massa = adc.channel(pin='P13',attn=ADC.ATTN_11DB)

#initiliaze float sensor (GPIO pull up)
pin_float_status = 1
pin_float = Pin('P0', mode=Pin.IN, pull=Pin.PULL_UP)
    #floatValue = 1 if not tripped
    #floatValue = 0 if tripped, send alarm

# initiliaze relay (GPIO)
pin_relay = Pin('P2',mode=Pin.OUT)
pin_relay.value(0)

#Initiliaze Sigfox
def sendMessage():
    #Sigfox
    sfx = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ2) # init Sigfox for RCZ2 (USA)
    s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW) # create a Sigfox Socket


    s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False) # configure it as uplink only
    s.send(str(massaHex))
    s.send(str(floatHex))
    print("Sigfox Message Sent")


while True:
    pin_relay.value(0)
    time.sleep(5) #wait for 5 seconds
    #if (counter)
    massaHex = "%04x" % pin_massa.value()
    floatHex = "%04x" % pin_float.value()
    #valueP13 = str(hex(pin_massa.value())).lstrip("0x")
    print("Massa Value(Hex):" + massaHex)
    print("Float Value:" + floatHex)


    sendMessage()
    pin_relay.value(1)

    #pin_float.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING, pin_high_handler, pin_float)

    time.sleep(60) #sleep for 30 mins
