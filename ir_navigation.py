# fast_IR_roaming

from cyberbot import *   
from feedback360 import *

drive.connect()
        
def forward():
    drive.speed(37, 37)
    sleep(20)

def backwards():
    drive.speed(-37, -37)
    sleep(20)

def right():
    drive.speed(37,0)
    sleep(20)

def left():
    drive.speed(0,37)
    sleep(20)

while True:
    irL = bot(14, 13).ir_detect(37500)
    irR = bot(1, 2).ir_detect(37500)
    
    if irL == 0 and irR == 0:                                      
        backwards()
    elif irL == 1 and irR == 0:                                   
        left()
    elif irL == 0 and irR == 1:                                 
        right()
    else:                                           
        forward()

