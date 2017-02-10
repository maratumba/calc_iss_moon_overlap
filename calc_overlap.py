#!/usr/bin/env python

import ephem
import datetime as dt
import math
import matplotlib.pyplot as plt

deg_per_rad=180. / math.pi

g=ephem.Observer()

#istanbul (kagithane gibi)
g.lat=41.068509
g.lon=28.932529
g.date=dt.date.today()

m=ephem.Moon()

iss=ephem.readtle('ISS',
                  '1 25544U 98067A   17054.09013250  .00016717  00000-0  10270-3 0  9161',
                  '2 25544  51.6375 247.0788 0006374 224.1226 135.9419 15.54417563  4001')

m_alt=[]
m_az=[]

iss_alt=[]
iss_az=[]

for i in range(24*15):
    iss.compute(g)
    m.compute(g)
    #calculate trajectory of the moon in 15 minute intervals
    
    m_alt.append(m.alt * deg_per_rad)
    m_az.append(m.az *  deg_per_rad)
    
    iss_alt.append(iss.alt *deg_per_rad)
    iss_az.append(iss.az * deg_per_rad)
    
    #calculate ISS trajectory in 15 minute intervals
    
    g.date += ephem.minute*15
    
    

