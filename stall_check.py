from cyberbot import *
from feedback360 import *
import math

# Expected pulse width deviation of 20/64ths per second
# 1/64th = 16 µs pulse delta (approx)
# Speed set to 20/64 of a turn per second
# 1/10 s -> 2/64ths of a turn -> 32 µs deviation
# Minimum deviation threshold set to 11, wich is in the
# neighborhood of 1/3 the expected deviation.

"""You pass check_stall the last tHL and tHR
and it compares those to the current ones. It returns
the new values, and a 1 if it stalled and a 0
if it's not
tHL = time high left
tHR = time high right 
These are proportional to the angle of the wheel"""

def check_stall(tHL0, tHR0):
    threshold = 11
    tHL = bot(16).pulse_in(1) #time high left
    tHR = bot(17).pulse_in(1) #time high right
    dtl = abs(int(tHL - tHL0)) #left difference
    dtr = abs(int(tHR - tHR0)) #right difference
    if (dtl < threshold)|(dtr < threshold):
        display.show(Image.SAD)
        stalled=1
    else:
        display.show(Image.HAPPY)
        stalled=0
    return(stalled, tHL, tHR)
