import pywhatkit
import os
import time
def whatsappmsg():
    t=time.localtime()
    t
    if t[4]==59:
        hours=t[3]+1
        minutes=0
    else:
        hours=t[3]
        minutes=t[4]+1
    pywhatkit.sendwhatmsg("+917357838067","Face Detected",hours,minutes)
    
    
