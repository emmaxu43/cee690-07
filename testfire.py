import pandas as pd
import numpy as np
import datetime 
from datetime import datetime, date
import glob

x= [1,2,3,4,5,6,7,8,9,10]
print(x[:5:],'and',x[6::])
exit()
"""lats= np.linspace(-84.65644,84.65644,1624)
lons= np.linspace(-179.95332,179.95332,3856)
smap_lat= df['lat']
smap_lon= df['lon']
ILAT=[]
ILON=[]
for lat in smap_lat:
  ilat= (1624-int(np.argmin(np.abs(lats-lat))))-150
  ILAT.append(ilat)
for lon in smap_lon:
  ilon= int(np.argmin(np.abs(lons-lon)))
  ILON.append(ilon)
df['ilat'] = ILAT
df['ilon'] = ILON
df.to_csv(file)
print(df.head())"""

"""SMAP_L4_SM_gph_20180601T013000_Vv4030_001.h5  
SMAP_L4_SM_gph_20180601T043000_Vv4030_001.h5
SMAP_L4_SM_gph_20180601T073000_Vv4030_001.h5
SMAP_L4_SM_gph_20180601T103000_Vv4030_001.h5
SMAP_L4_SM_gph_20180601T133000_Vv4030_001.h5
SMAP_L4_SM_gph_20180601T163000_Vv4030_001.h5
SMAP_L4_SM_gph_20180601T193000_Vv4030_001.h5
SMAP_L4_SM_gph_20180601T223000_Vv4030_001.h5"""
 
