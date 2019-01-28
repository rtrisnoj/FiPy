
from machine import ADC
from machine import Pin
from network import Sigfox
from deepsleep import DeepSleep
import socket
import time
import binascii

#initiliaze massa sensor configuration (ADC)
adc = ADC()
adc.vref(3130)

p13 = adc.channel(pin='P13',attn=ADC.ATTN_11DB)

#initiliaze float sensor (GPIO pull up)
p0 = Pin('P0',mode=Pin.IN, pull=Pin.PULL_UP)
    #floatValue = 1 if not tripped
    #floatValue = 0 if tripped, send alarm

# initiliaze relay (GPIO)
p2 = Pin('P2',mode=Pin.OUT)
p2.value(0)

#Initiliaze Sigfox
def sendMessage():
    #Sigfox
    sfx = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ2) # init Sigfox for RCZ2 (USA)
    #sfx.config()
    #import binascii
    #print(binascii.hexlify(sfx.id()))
    #print(binascii.hexlify(sfx.pac()))
    s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW) # create a Sigfox Socket
    #s.setblocking(True) #make the socket blocking
    s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False) # configure it as uplink only
    s.send(str(P13.value()))
    #s.send(str(p0.value()))



while True:
    p2.value(0)
    time.sleep(5) #wait for 5 seconds
    #if (counter)
    temp1 = "%04x" % p13.value()
    temp2 = "%04x" % p0.value()
    valueP13 = str(hex(p13.value())).lstrip("0x")
    #print(valueP13.ljust(4, '0'))
    print("Massa Value(Hex):" + temp1)
    #print (valueP13)
    print("Float Value:" + temp2)
    #print("Massa value:" + str(P13.value()))
    #print("Float value:" + str(p0.value()))

    #sendMessage()

    p2.value(1)
    time.sleep(295) #sleep for 30 mins
