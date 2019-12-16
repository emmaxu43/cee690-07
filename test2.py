import sklearn.tree
import sklearn.model_selection
import sklearn.ensemble
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import norm

file= "/home/cx43/cee690-07/data/2018fire/test2_fire.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)
vars= ['burnedarea','v10wind','u10wind','sm_surface','sTemp','Wind','elevation','nlcd','evi','vwc']
#STANDARLIZATION ##########firename	date	ID	burnedarea	lon	lat	v10wind	u10wind	ilat	ilon	sm_surface	sTemp	Wind	ilat_tif	ilon_tif	elevation	nlcd	ilat_evi	ilon_evi	evi##############################
vars= ['v10wind','u10wind','sm_surface','sTemp','Wind','elevation','nlcd','evi','vwc']
for var in vars:
  tmp1= df[var]  #len=306
  tmp= np.array(tmp1)
  tmp_sd= (tmp-np.mean(tmp,axis=0))/np.std(tmp,axis=0)  #len=306
  df[var]= tmp_sd
  print(df[var].size)
df.to_csv(file)

############random forest for 8 predictor###############
data={}
DATA=[]
for var in vars:
  data[var]= np.array(df[var])  #(306,)
  DATA.append(data[var])
dataset= np.array(DATA).reshape(306,9)

tmp= np.array(df['burnedarea'])
obs_fire= np.array(tmp)  # (306,)

#define kfolds -> 10 folds
kf = sklearn.model_selection.KFold(n_splits=10,shuffle=True,random_state=1)
#clf= sklearn.tree.DecisionTreeClassifier(random_state=1)
bclf = sklearn.ensemble.RandomForestClassifier(n_estimators=500,oob_score=True,random_state=1)
obs_fire= obs_fire.astype('int')

#fit a decision tree
bclf= bclf.fit(dataset,obs_fire)

scores= sklearn.model_selection.cross_val_score(bclf,dataset,obs_fire,cv=kf)
print('All data:',np.mean(scores))  
#All data: 0.07161290322580645 using 500 decision trees

#feature importance
print(bclf.feature_importances_,'\n',)
#[0.13144738 0.12130209 0.12888106 0.11477502 0.12360702 0.12119536 0.12787473 0.13091734]
x= np.linspace(1,9,9)
plt.plot(x,bclf.feature_importances_)
plt.title('feature importance')
plt.xticks(x, vars, rotation=45)
plt.ylabel('feature importance')
#plt.savefig('/home/cx43/cee690-07/data/2018fire/feature_importance.png')
plt.show()
  



