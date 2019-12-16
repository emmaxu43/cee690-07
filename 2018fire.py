from __future__ import division
import time
import pandas as pd
import numpy as np
import datetime 
from datetime import datetime, date
import glob
import netCDF4 as nc
import xarray as xr
import matplotlib.pyplot as plt
import time

#####################get SMAP paths#############################################################
tic= time.time()
file= "/home/cx43/cee690-07/data/2018fire/testfire.csv"
dataset= pd.read_csv(file)
#print(data.shape)  #(322, 9)-> 313
df = pd.DataFrame(dataset)

time_csv= df['date']
time_tmp1= pd.Series.to_string(time_csv,index= False)
#print(time.size,len(tmp))  #313 #9389 w/ index -> 7511 w/o index
format= '  %m/%d/%Y %I:%M:%S %p'
time_tmp2= time_tmp1.split('\n')
#print(time_tmp2)  #'  11/14/2018 2:30:00 PM'

time_list= ['013000','043000','073000','103000','133000','163000','193000','223000']
format_time= '%H%M%S'
new_time={}
new={}
for i in range(7):
  new_time[i]= datetime.strptime(time_list[i],format_time)
  new[i]= new_time[i].time()

strs= glob.glob("/stor/tyche/hydro/private/cx43/CEE675_2019Fall/project2/smap/data/*.h5")
files= sorted(strs)

FILES=[]
TIME=[]
k=0
for tmp in time_tmp2:
    new_date= datetime.strptime(tmp, format)
    #print(new_date.strptime(format))
    tmp1= new_date.date()
    tmp2= new_date.time()
    #print('Date:', new_date.date())  #Date: 2018-11-18
    #print('Time:', new_date.time())  #Time: 21:00:00
    date_tmp= tmp1.strftime('%Y%m%d')
    time_tmp= tmp2.strftime('%H%M%S')
    for single_file in files:
      tmp_file= ('/stor/tyche/hydro/private/cx43/CEE675_2019Fall/project2/smap/data/SMAP_L4_SM_gph_%sT223000_Vv4030_001.h5' % date_tmp)
      if tmp_file== single_file: FILES.append(date_tmp)
    #print(len(FILES)) #306

    delta={}
    for i in range(7):
      delta[i]= datetime.combine(date.min, new[i]) - datetime.combine(date.min, tmp2)
      threshold= delta[i].total_seconds()
      if threshold<5400.0: 
        new_tmp= new[i].strftime('%H%M%S')
        TIME.append(new_tmp)
    k += 1
#print(len(TIME),TIME,k)      #len=1530,k= 306
NEW_TIME= TIME[::5]
#print(NEW_TIME,len(NEW_TIME)) #LEN= 306

SMAP_FILE=[]
for i in range(len(NEW_TIME)):
  tmp_file= ('/stor/tyche/hydro/private/cx43/CEE675_2019Fall/project2/smap/data/SMAP_L4_SM_gph_%sT%s_Vv4030_001.h5' % (FILES[i],NEW_TIME[i]))
  SMAP_FILE.append(tmp_file)
#print(len(SMAP_FILE)) #306
SMAP= sorted(SMAP_FILE)
#print(SMAP)
tmp= time.time()-tic
print("checkpoint 1 = ",tmp)  #0.3s

############################append SMAP sm_surface into FIRE DATA#################################
"""tic= time.time()
var= 'sm_surface'
SM=[]
tmp_ilat= df['ilat']
tmp_ilon= df['ilon']
ilat= np.array(tmp_ilat)
ilon= np.array(tmp_ilon)

i=0
for path in SMAP:
  fp = xr.open_dataset(path,group='Geophysical_Data' )
  tmp_data= fp[var][:]  #globally, (1624, 3856) -> y,x
  data= np.array(tmp_data)
  smap_tmp= data[ilat[i],ilon[i]]
  SM.append(smap_tmp)  # len(SM)= 306
  i +=1
tmp= time.time()-tic
print("checkpoint 2 = ",tmp) #87s

tic= time.time()
df['sm_surface'] = SM
df.to_csv(file)
print(df.head())
tmp= time.time()-tic
print("checkpoint 3 = ",tmp)  # 0.05s"""

############################append SMAP T,windSPEED into FIRE DATA#################################
tic= time.time()
vars= ['surface_temp','windspeed_lowatmmodlay']
ST=[]
WSP=[]
TMP=[]
tmp_ilat= df['ilat']
tmp_ilon= df['ilon']
ilat= np.array(tmp_ilat)
ilon= np.array(tmp_ilon)
i=0
for path in SMAP:
  fp = xr.open_dataset(path,group='Geophysical_Data' )
  for var in vars:
    tmp_data= fp[var][:]
    data= np.array(tmp_data)
    smap_tmp= data[ilat[i],ilon[i]]
    TMP.append(smap_tmp)
  i +=1
#print(len(TMP))  #612
tmp= time.time()-tic
print("checkpoint 4 = ",tmp)  #123s

tic= time.time()
ST= TMP[:306:]
WSP = TMP[306::]
df['sTemp'] = ST
df['Wind'] = WSP
df.to_csv(file)
tmp= time.time()-tic
print("checkpoint 5 = ",tmp)  