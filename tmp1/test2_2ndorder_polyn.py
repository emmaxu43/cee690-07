import pandas as pd
import numpy as np
import pymc3 as pm
import time
import matplotlib.pyplot as plt
#11:17 min

vars= ['fireClass','v10wind','u10wind','sm_surface','sTemp','Wind','elevation','nlcd','evi','vwc']
file= "/home/cx43/cee690-07/data/2018fire/test2_fire_Nov29.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)
tmp={}
data=[]
for var in vars:
  tmp[var]= df[var]


predictors= ['v10wind','u10wind','sm_surface','sTemp','Wind','elevation','nlcd','evi','vwc']

new_predictors= predictors.copy()
for i,var1 in enumerate(predictors):
    for j,var2 in enumerate(predictors[i::]):
        name= '{0}*{1}'.format(var1,var2)
        df[name]= df[var1]*df[var2]
        new_predictors.append(name)

multiple_model= pm.Model()

with multiple_model:
    intercept = pm.Normal('intercept',mu=0,sd=100)
    beta = pm.Normal('beta',shape= len(new_predictors),sd=100) 
    variance = pm.InverseGamma('variance',alpha=0.1,beta=0.1)
    sd       = pm.Deterministic('sd',variance**0.5)
    
    yhat = pm.Deterministic('yhat',intercept + pm.math.dot(df[new_predictors], beta))
    #yhat = intercept + pm.math.dot(df[predictors],beta)
    y    = pm.Normal('y',mu=yhat,sd=sd, observed=df['fireClass'])

with multiple_model:
    step = pm.NUTS()
    trace = pm.sample(step=step,tune=2000,draws=2000,chains=4)

with multiple_model: 
    print(pm.stats.r2_score(df['fireClass'].values,trace[yhat]))

y_pred= trace['yhat'][1]
y_true= df['fireClass']

x= np.linspace(0,305,306)
plt.plot(x,y_pred)
plt.plot(x,y_true)
plt.ylabel('fire class')
plt.xlabel('fire event')
plt.title('polynomial')
plt.show()
