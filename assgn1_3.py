# Name: Assignment_1_3
# Purpose: Write a class that returns an instance that contains the data
# Function: read_burl()
# Input: file
# Output: dates, pressure, v_wind, u_wind
# Author and history: Yue Wang  09/11/2013

import numpy as np                  # import numpy
from datetime import datetime

class read_burl():
    
    def __init__(self,file):
        self.data     = file
        data          = open(self.data)
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
        
        self.dates = np.array(dates)
        self.pressure = np.array(pressure)
        self.u_wind = np.array(u_wind)
        self.v_wind = np.array(v_wind)
        
    
    
if __name__ == "__main__":                 
    value_c = read_burl('burl1_2011.txt')
    
print 'datetime =', value_c.dates[10]
print 'pressure =',value_c.pressure[10]
print 'u_wind =',value_c.u_wind[10]
print 'v_wind =',value_c.v_wind[10]


