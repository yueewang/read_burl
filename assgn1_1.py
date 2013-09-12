## Name: Assignment_1_1
# Purpose: Write a script that reads the Burl 1 historical wind data
# Input: burl1_2011.txt
# Output: dates, pressure, v_wind, u_wind
# Author and history: Yue Wang  09/10/2013

import numpy as np                  # import numpy
from datetime import datetime


data = open('burl1_2011.txt')       # read data

dates         = []                  #identify variable
pressure      = []
winds         = []
windd         = []
v_wind        = []
u_wind        = []
winddo        = []

for line in data.readlines()[2:]:  #read lines
    data0 = line.split()
    year  = int(data0[0])
    month = int(data0[1])
    day   = int(data0[2])
    hour  = int(data0[3])
    minute= int(data0[4])
    windd.append(float(data0[5]))
    winds.append(float(data0[6]))
    pressure.append( float(data0[12]) )
    dates.append(datetime(year, month, day, hour, minute))
    
windd     = np.array(windd)       #convert to array
winds     = np.array(winds)

winddo    = windd  * (np.pi/180)  #calculate
u_wind    = -winds * np.sin(winddo)
v_wind    = -winds * np.cos(winddo)

value = {'dates': np.array(dates),'pressure': np.array(pressure),'u_wind':u_wind,'v_wind':v_wind}

print value['dates']              #print the data
print value['pressure']
print value['u_wind']
print value['v_wind']




   
    




