from __future__ import division
import time
import pandas as pd
import numpy as np
import datetime 
from datetime import datetime, date, timedelta
import glob
import netCDF4 as nc
import xarray as xr
import matplotlib.pyplot as plt

paths= glob.glob('/stor/tyche/hydro/private/cx43/CEE675_2019Fall/project2/ndvi/data/*')
EVI= sorted(paths) #16days
#print(len(EVI),EVI)  #14

minlon= -130.540728914638
maxlon= -103.699828723654
minlat= 29.8308028608368
maxlat= 40.0852255853565 

file_idx= np.linspace(145,353,14)
IDX=[]
for i in range(file_idx.size):
  tmp1= int(file_idx[i])
  tmp= str(tmp1)
  IDX.append(tmp)  #['154','170'...]
####################ILAT,ILON#######################################  
file= "/home/cx43/cee690-07/data/2018fire/2018fire.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)

"""lats= np.linspace(minlat,maxlat,4800)
lons= np.linspace(minlon,maxlon,4800)
lat_csv= df['lat']
lat= np.array(lat_csv)
lon_csv= df['lon']
lon= np.array(lon_csv)
ILAT=[]
ILON=[]
i=0
for i in range(lat.size):
  ilat= int(np.argmin(np.abs(lats-lat[i])))
  ilon= int(np.argmin(np.abs(lons-lon[i])))
  ILAT.append(ilat)
  ILON.append(ilon)
  i +=1

df['ilat_evi'] = ILAT
df['ilon_evi'] = ILON
df.to_csv(file)"""

######################read the right MOD13 file#####################################
time_csv= df['date']
time_tmp1= pd.Series.to_string(time_csv,index= False)
format= '  %m/%d/%Y %I:%M:%S %p'
time_tmp2= time_tmp1.split('\n')  #'  11/14/2018 2:30:00 PM'

format_date='%m/%d/%Y'
FIRE_DATE=[]
for tmp in time_tmp2:
  new_date= datetime.strptime(tmp, format)
  tmp1= new_date.date()
  date_tmp= tmp1.strftime(format_date)
  FIRE_DATE.append(date_tmp)  # ['11/17/2018',..., '11/14/2018', ]

base = date(2018, 5, 25)  #2018-5-25
date_list = [base + timedelta(days=x) for x in range(16*14)]
tmp_date= date_list[::16]  # [datetime.date(2018, 5, 25), datetime.date(2018, 6, 10)..]
EVI_date=[]
for x in tmp_date:
  x1= x.strftime('%m/%d/%Y')
  EVI_date.append(x1)  #['05/25/2018', '06/10/2018'..] -> 14
  
PLACE_TMP=[]
i=0
for i in range(14):
  datetime.strptime(EVI_date[i], format_date)
  tmp1= new_date.date()
  for j in range(306):
    datetime.strptime(FIRE_DATE[j], format_date)
    tmp2= new_date.date()  
    delta= (tmp1 - tmp2).days
    if delta<8: PLACE_TMP.append(i)
#print(PLACE_TMP,len(PLACE_TMP))  #len=4284 
PLACE_HOLDER= PLACE_TMP[::14]
#print(len(PLACE_HOLDER)) # 306

i=0
ilat= df['ilat_evi']
ilon= df['ilon_evi']
EVI_VALUES=[] 
for idx in PLACE_HOLDER:
  print(idx)
  path= EVI[idx]
  fp= xr.open_dataset(path)
  tmp_data= fp['250m 16 days EVI'][:]  # shape= (4800,4800)
  tmp= np.array(tmp_data)
  data= tmp[ilat[i],ilon[i]]
  i +=1
  EVI_VALUES.append(data)
  if i== 306: break
print(len(EVI_VALUES))
df['evi'] = EVI_VALUES
df.to_csv(file)
  
  
  


"""date:5_25  
6_10  6_26  
7_12  7_28
8_13  8_29
9/_14  9_30
10_16
11_1  11_17
12_3  12_19
['../data/MOD13Q1.A2018145.h08v05.006.2018162000452.hdf', '../data/MOD13Q1.A2018161.h08v05.006.2018177235938.hdf', '../data/MOD13Q1.A2018177.h08v05.006.2018197102822.hdf', '../data/MOD13Q1.A2018193.h08v05.006.2018210001605.hdf', '../data/MOD13Q1.A2018209.h08v05.006.2018227125622.hdf', '../data/MOD13Q1.A2018225.h08v05.006.2018242000006.hdf', '../data/MOD13Q1.A2018241.h08v05.006.2018258000444.hdf', '../data/MOD13Q1.A2018257.h08v05.006.2018282125616.hdf', '../data/MOD13Q1.A2018273.h08v05.006.2018295105634.hdf', '../data/MOD13Q1.A2018289.h08v05.006.2018313115921.hdf', '../data/MOD13Q1.A2018305.h08v05.006.2018321225857.hdf', '../data/MOD13Q1.A2018321.h08v05.006.2018338084403.hdf', '../data/MOD13Q1.A2018337.h08v05.006.2018365153713.hdf', '../data/MOD13Q1.A2018353.h08v05.006.2019032133550.hdf']"""
