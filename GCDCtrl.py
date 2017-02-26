# -*- coding: utf-8 -*-
#GCD-0301M
import serial
import time   #set delay
#import io
ser1=serial.Serial()
ser1.port='COM6'   #电控平台端口6 黑线
ser1.baudrate=19200
ser1.open()



ser1.write('@1D01\r\n')#设置步进方向0 @1D00/1
time.sleep(0.5)

'''
print ser1.inWaiting()
data = ''
while ser1.inWaiting() > 0:
    data += ser1.read(1)
if data != '':
    print data

'''

ser1.write('@1SEF\r\n')#设置步进速度 01-FF
time.sleep(0.5)
ser1.write('@1P000000FF\r\n')#设置步进脉冲数 FF FF FF FF
time.sleep(0.5)
i=1
while i<=2:
    ser1.write('@0G\r\n')
    time.sleep(2)
    i=i+1


ser1.close()
#print ser1