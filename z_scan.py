# -*- coding: utf-8 -*-
#z-scan
import math
import numpy as np
import serial
import time   #set delay

def YiChang(x):
    xba=np.average(x)
    xi=x-xba
    sigma=math.sqrt(sum(xi*xi)/(len(x)-1))
    s=xi[abs(xi)<=3*sigma]+xba
    return np.average(s)
    
    
ser1=serial.Serial()
ser1.port='COM6'   #电控平台端口6 黑线
ser1.baudrate=19200
ser1.open()

ser2=serial.Serial()
ser2.port='COM7'  #功率计端口7 银线
ser2.baudrate=9600
ser2.rtscts=False  #different from VB
ser2.dsrdtr=False
ser2.open()

ser1.write('@1D01\r\n')#设置步进方向0 @1D00/1
time.sleep(0.5)
ser1.write('@1SEF\r\n')#设置步进速度 01-FF
time.sleep(0.5)
ser1.write('@1P000000FF\r\n')#设置步进脉冲数 FF FF FF FF
time.sleep(0.5)
i=1
k=3                 # set measure times
store=np.zeros((k,3))
#loop




while i<=k:         # set measure times
    ser1.write('@0G\r\n') #motor go
    time.sleep(2)         #set waiting time about 5-10seconds
    temp=np.zeros((30,2))
    for j in range(30):
        ser2.write('$SB\r')   # sent data both A B
        time.sleep(0.2)
        data = ''
        while ser2.inWaiting() > 0:
            data += ser2.read(1)
       # if data != '':
        #    print data
        if len(data)==23:
            Ao=float(data[2:11])
            Bo=float(data[13:21])
            temp[j,0]=Ao
            temp[j,1]=Bo
        else:
            temp[j,:]=0    
    store[i,0]=YiChang(temp[:,0])  #第一列为一号口的平均值
    store[i,1]=YiChang(temp[:,1])  #第二列为二号口的平均值  
    store[i,2]=store[i,0]/store[i,1]  #比值  
        
    i=i+1
print store

np.savetxt('Laser.csv',store,delimiter=',')


ser1.close()
ser2.close()