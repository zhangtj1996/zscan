import numpy as np
temp=np.zeros((30,2))
for j in range(30):
    ser2.write('$SB\r')   # sent data both A B
    time.sleep(0.2)
    data = ''
    while ser2.inWaiting() > 0:
        data += ser2.read(1)
    if data != '':
        print data
    if len(data)==23:
        Ao=float(data[2:11])
        Bo=float(data[13:21])
        temp[j,0]=Ao
        temp[j,1]=Bo
          