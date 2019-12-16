import sklearn.tree
import sklearn.model_selection
import sklearn.ensemble
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file= "/home/cx43/cee690-07/data/2018fire/test2_fire_Nov29.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)

vars= ['v10wind','u10wind','sm_surface','sTemp','Wind','elevation','nlcd','evi','vwc']

data={}
DATA=[]
for var in vars:
  data[var]= np.array(df[var])  #(306,)
  DATA.append(data[var])
dataset= np.array(DATA).reshape(306,9)

tmp= np.array(df['fireClass'])   #df['burnedarea'])
obs_fire= np.array(tmp) 

#define kfolds -> 10 folds
kf = sklearn.model_selection.KFold(n_splits=10,shuffle=True,random_state=1)
#clf= sklearn.tree.DecisionTreeClassifier(random_state=1)

"""S=[]
for i in range(1,200):
  bclf = sklearn.ensemble.RandomForestClassifier(n_estimators=i,oob_score=True,random_state=1)
  obs_fire= obs_fire.astype('int')

#fit a decision tree
  bclf= bclf.fit(dataset,obs_fire)
  S.append(bclf.oob_score_)

x= np.arange(199)
plt.plot(x+1,S)
plt.xlabel('number of decision trees')
plt.ylabel('out of bag score')
plt.show()"""


bclf = sklearn.ensemble.RandomForestClassifier(n_estimators=150,oob_score=True,random_state=1)
obs_fire= obs_fire.astype('int')
bclf= bclf.fit(dataset,obs_fire)
print(bclf.oob_score_)
ypred= bclf.predict(dataset)

# plot pred vs. true
#ypred= bclf.predict(obs_fire)
x= np.linspace(0,306,306)
plt.figure(figsize=(15,15))
plt.plot(x,ypred,'g--')
plt.plot(x,obs_fire,'r:')
plt.title('random forests',fontsize=15)
plt.ylabel('fire class', fontsize=15)
plt.xlabel('fire event',fontsize=15)
plt.legend(['Prediction','Observation'])
plt.show()