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

"""paths= glob.glob('/stor/tyche/hydro/private/cx43/CEE675_2019Fall/project2/ndvi/data/*')
EVI= sorted(paths) #16days

minlon= -130.540728914638
maxlon= -103.699828723654
minlat= 29.8308028608368
maxlat= 40.0852255853565 

file_idx= np.linspace(145,353,14)
IDX=[]
for i in range(file_idx.size):
  tmp1= int(file_idx[i])
  tmp= str(tmp1)
  IDX.append(tmp)"""
####################ILAT,ILON#######################################  
file= "/home/cx43/cee690-07/data/2018fire/test1_fire.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)

######################read the right MOD13 file#####################################
"""time_csv= df['date']
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
  tmp_data= fp['250m 16 days NDVI'][:]  # shape= (4800,4800)
  tmp= np.array(tmp_data)
  data= tmp[ilat[i],ilon[i]]
  i +=1
  EVI_VALUES.append(data)
  if i== 306: break
print(len(EVI_VALUES))
df['ndvi'] = EVI_VALUES
df.to_csv(file)

###############stem factor###########################
nlcd= np.array(df['nlcd'])
nlcd_list= np.unique(nlcd)
#print(nlcd_list)  #[21 22 42 52 71 82] -> [0,0,19.15,1.5,1.5,3.5]

s_factor= np.copy(nlcd)
factor= [0,0,19,2,2,4]
m1= s_factor==21
s_factor[m1]= 0
m5= s_factor==22
s_factor[m5]= 0
m2= s_factor==42
s_factor[m2]= 19
m3= s_factor==52
s_factor[m3]== 2 
m6= s_factor==72
s_factor[m6]== 2
m4= s_factor==82
s_factor[m4]= 4
df['stem_factor'] = s_factor
df.to_csv(file)"""

#################compute vwc##############################
"""stem_factor= np.array(df['stem_factor'])
ndvi= np.array(df['ndvi'])
ndvi_max= np.max(ndvi)
ndvi_min= np.min(ndvi)
vwc= (1.9134*ndvi**2-0.3215*ndvi)+stem_factor*((ndvi_max-ndvi_min)/(1-ndvi_min))
#print(vwc.shape) #306
print(ndvi_max,ndvi_min) #49760000 7270000
df['vwc']= vwc
df.to_csv(file)"""

############standarlize vwc#########
vwc= np.array(df['vwc'])
vwc_std= (vwc- np.mean(vwc,axis=0))/np.std(vwc,axis=0)
print(np.mean(vwc,axis=0),np.std(vwc,axis=0)) #658279571895424.9   719560163450646.1

df['vwc_std']= LIST
df.to_csv(file)


  
