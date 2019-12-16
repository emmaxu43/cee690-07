import rasterio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

######################################NED############################
"""fp1= rasterio.open("/stor/tyche/hydro/private/cx43/CEE675_2019Fall/project2/data/elevation.tif")  #Size is 452, 409
dataset= fp1.read(1)
data = np.ma.masked_array(dataset,dataset==0)
fp1.close()

file= "/home/cx43/cee690-07/data/2018fire/2018fire.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)
"""
"""lons= np.linspace(-125.9100000,-113.7060000,452)
y_tmp= np.linspace(32.1570000,43.2000000,409)
lats= y_tmp[::-1]

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

df['ilat_tif'] = ILAT
df['ilon_tif'] = ILON
df.to_csv(file)"""

"""lat_csv= df['ilat_tif']
ilat= np.array(lat_csv)
lon_csv= df['ilon_tif']
ilon= np.array(lon_csv)
TMP=[]
for i in range(306):
  ned_tmp= data[ilat[i],ilon[i]]
  TMP.append(ned_tmp)
df['elevation'] = TMP
df.to_csv(file)"""

#####################################NLCD############################
fp2= rasterio.open("/stor/tyche/hydro/private/cx43/CEE675_2019Fall/project2/data/landcover.tif")  # Size is 452, 409
dataset= fp2.read(1)
data = np.ma.masked_array(dataset,dataset==0)
fp2.close()

plt.imshow(data)
plt.title('NLCD 2016')
plt.show()
exit()

file= "/home/cx43/cee690-07/data/2018fire/2018fire.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)

lat_csv= df['ilat_tif']
ilat= np.array(lat_csv)
lon_csv= df['ilon_tif']
ilon= np.array(lon_csv)
TMP=[]
for i in range(306):
  ned_tmp= data[ilat[i],ilon[i]]
  TMP.append(ned_tmp)
df['nlcd'] = TMP
df.to_csv(file)
exit()

"""print(data)  #elevation
[[-- -- -- ... 1426.6666259765625 1425.8807373046875 1434.4676513671875]
 [-- -- -- ... 1435.0848388671875 1416.974365234375 1409.799072265625]
 [-- -- -- ... 1431.7435302734375 1416.7322998046875 1399.9149169921875]
 ...
 [-- -- -- ... 378.3800048828125 364.0141296386719 350.8150939941406]
 [-- -- -- ... 367.7654724121094 402.775634765625 372.4364013671875]
 [-- -- -- ... 375.25762939453125 507.8045654296875 467.9912109375]]
plt.imshow(data)
plt.title('elevation')
plt.show()"""

"""print(data)
 code: 20
[[-- -- -- ... 52 52 52]
 [-- -- -- ... 52 52 52]
 [-- -- -- ... 71 52 52]
 ...
 [-- -- -- ... 52 52 52]
 [-- -- -- ... 52 31 52]
 [-- -- -- ... -- -- 52]]
plt.imshow(data)
plt.title('landcover')
plt.show()"""
