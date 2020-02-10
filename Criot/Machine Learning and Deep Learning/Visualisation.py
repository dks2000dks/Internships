from __future__ import print_function

import numpy as np
from numpy import loadtxt
import pandas as pd
import math
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt


df = pd.read_csv('Data with Time Stamp.csv',sep=',')
#print (df.head())
Time = df['Time'].to_numpy()


Time_Stamp_Decoded = []
Date_Stamp_Decoded = []

for t in Time:
    x = t.split()
    Date = x[0] + ' '
    S = x[1].split(':')

    Stamp = int(S[0]) + (1/60)*int(S[1])

    Time_Stamp_Decoded.append(Stamp*2)
    Date_Stamp_Decoded.append(Date)

#print (Date_Stamp_Decoded)
#print (Time_Stamp_Decoded)


A = df['A'].to_numpy()
B = df['B'].to_numpy()
C = df['C'].to_numpy()
D = df['D'].to_numpy()
E = df['E'].to_numpy()

DataA = []
DataB = []
DataC = []
DataD = []
DataE = []
Time_Stamp = []
Date_Stamp = []
Check = 1
a = 0
b = 0
c = 0
d = 0
e = 0
n = 0

for i in range(A.shape[0]):
    if Check == 1:
        t = int(Time_Stamp_Decoded[i])
        date = Date_Stamp_Decoded[i]
        Check = 0

    if (t == int(Time_Stamp_Decoded[i])):
        n += 1
        a += int(A[i])
        b += int(B[i])
        c += int(C[i])
        d += int(D[i])
        e += int(E[i])


    else:
        DataA.append(a/n)
        DataB.append(b/n)
        DataC.append(c/n)
        DataD.append(d/n)
        DataE.append(e/n)
        Time_Stamp.append(str(t/2))
        Date_Stamp.append(date)

        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        n = 0

        t = int(Time_Stamp_Decoded[i])
        date = Date_Stamp_Decoded[i]
        n = 1
        a += int(A[i])
        b += int(B[i])
        c += int(C[i])
        d += int(D[i])
        e += int(E[i])

PIR = DataA
Intensity = DataB
Gas_Sensor = DataC
Temperature = list((np.array(DataD) + np.array(DataE))/2)
Date_and_Time = []
for i in range(len(Time_Stamp)):
    Date_and_Time.append(Date_Stamp[i] + Time_Stamp[i])

def Plot(x,y,label):
	plt.figure(figsize=(20,15))
	plt.plot(x,y)
	plt.xlabel('Date and Time Stamp')
	plt.ylabel(label)
	plt.xticks(rotation=90,fontsize=8)

	plt.savefig(label + ".jpeg")
	plt.show()

Plot(Date_and_Time,PIR,"PIR")
Plot(Date_and_Time,Intensity,"Intensity")
Plot(Date_and_Time,Gas_Sensor,"Gas_Sensor")
Plot(Date_and_Time,Temperature,"Temperature")
