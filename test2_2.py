import sklearn.tree
import sklearn.model_selection
import sklearn.ensemble
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import norm

file= "/home/cx43/cee690-07/data/2018fire/2018fire_copy.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)
vars= ['burnedarea','v10wind','u10wind','sm_surface','sTemp','Wind','elevation','nlcd','evi','vwc']

data={}
i=0
cdf_5=[]
cdf_95=[]
for var in vars:
  i += 1
  plt.subplot(5,2,i)
  data[var]= np.array(df[var])
  plt.hist(data[var],100)
  tmp_5= np.percentile(data[var],5)
  tmp_95= np.percentile(data[var],95)
  #plt.legend([tmp_5,tmp_95])
  cdf_5.append(tmp_5)
  cdf_95.append(tmp_95)
  plt.title(var)
plt.tight_layout()
print(cdf_5,cdf_95)
#[0.60414002, 0.34616751100000004, 0.154218418, 0.040648266749999995, 274.5514083, 1.5187782349999999, 39.07733917, 42.0, 6010000.0, 176000000000000.0] 
#[850.0633211249999, 8.527762837000001, 3.497788462, 0.13341191424999999, 309.83816525, 6.182275057, 2651.592041, 82.0, 23190000.0, 1910000000000000.0]

plt.savefig('/home/cx43/cee690-07/data/2018fire/histogram.png')
plt.show()
