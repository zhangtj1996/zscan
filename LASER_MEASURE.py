# -*- coding: utf-8 -*-
import string
import serial
import time   #set delay
#ser2 laser measurement
ser2=serial.Serial()
ser2.port='COM7'  #功率计端口7 银线
ser2.baudrate=9600
ser2.rtscts=False  #different from VB
ser2.dsrdtr=False
ser2.open()
#ser2.flushInput()

strCmd='SB'
Fullcmd='$'+strCmd+chr(13)
ser2.write(Fullcmd)
time.sleep(0.2)
data = ''
while ser2.inWaiting() > 0:
    data += ser2.read(1)
if data != '':
    print data
if len(data)==23:
    Ao=float(data[2:11])
    Bo=float(data[13:21])
    print Ao
    print Bo
else:
    Ao=0
    Bo=0
    

ser2.close()

#print ser2