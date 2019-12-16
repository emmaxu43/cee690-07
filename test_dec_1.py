import sklearn.tree
import sklearn.model_selection
import sklearn.ensemble
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.decomposition

file= "/home/cx43/cee690-07/data/2018fire/test2_fire_Nov29.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)
vars= ['v10wind','u10wind','sm_surface','sTemp','Wind','elevation','nlcd','evi','vwc']

fire= df['fireClass']
tmp= np.array(fire)
#print(tmp)


#############FIRE CLASS DISTRIBUTION###############
x = np.arange(4)
x2= 0.44
x3= 0.56
x4= 0.93
x5= 0.77

y= x2+x3+x4+x5
y= [x2/y,x3/y,x4/y,x5/y] 


plt.bar(x,y)
plt.xticks(x,('B','C','D','E'))
plt.xlabel('Fire Class')
plt.ylabel('Probability')
plt.title('Wild Fire Class Distribution')
plt.show()
exit()

plt.figure(figsize=(10,10))
weights = np.ones_like(tmp)/float(len(tmp))
plt.hist(tmp,8,weights= weights, density= True)
plt.title('Wild Fire Class Distribution',fontsize=15)
plt.xlabel('Fire Class',fontsize=15)
plt.ylabel('Probability',fontsize=15)
plt.savefig('/home/cx43/cee690-07/data/fireclass.png')
plt.show()
exit()

###################PREDICTORS DISTRIBUTION#############
data={}
i=0
cdf_5= [0.34616751100000004, 0.154218418, 0.040648266749999995, 274.5514083, 1.5187782349999999, 39.07733917, 42.0, 6010000.0, 176000000000000.0] 
cdf_95= [8.527762837000001, 3.497788462, 0.13341191424999999, 309.83816525, 6.182275057, 2651.592041, 82.0, 23190000.0, 1910000000000000.0]

names= ['Vertical Wind (m/s)','Horizontal Wind (m/s)','Surface Soil Moisture (m3/m3)','Surface Temp (K)','Surface Wind (m/s)','Elevation (m)','Land Cover','EVI','VWC (m3/m3)']
i=1
for var in vars:
  k=100
  data[var]= np.array(df[var])
  plt.hist(data[var],k)
  x= np.linspace(cdf_5[i-1],cdf_95[i-1],k)
  y= np.zeros((k,))
  plt.plot(x,y,color='green')
  plt.title(names[i-1])
  plt.xlabel('Values of %s' % names[i-1])
  plt.ylabel('Frequency')
  plt.show()
  i +=1



