import sklearn.tree
import sklearn.model_selection
import sklearn.ensemble
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.decomposition

file= "/home/cx43/cee690-07/data/2018fire/test2_fire.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)
vars= ['v10wind','sm_surface','elevation','nlcd','vwc']

############random forest for 8 predictor###############
data={}
DATA=[]
for var in vars:
  data[var]= np.array(df[var])  #(306,)
  DATA.append(data[var])
dataset= np.array(DATA).reshape(306,5)

##########################pca#########################
pca = sklearn.decomposition.PCA(n_components=5)
pca.fit(dataset)
print(np.sum(pca.explained_variance_ratio_))
dataset_pca = pca.transform(dataset)

tmp= np.array(df['fireClass'])   #df['burnedarea'])
obs_fire= np.array(tmp)  # (306,)

#define kfolds -> 10 folds
kf = sklearn.model_selection.KFold(n_splits=10,shuffle=True,random_state=1)
#clf= sklearn.tree.DecisionTreeClassifier(random_state=1)
bclf = sklearn.ensemble.RandomForestClassifier(n_estimators=500,oob_score=True,random_state=1)
obs_fire= obs_fire.astype('int')

#fit a decision tree
bclf= bclf.fit(dataset_pca,obs_fire)

scores= sklearn.model_selection.cross_val_score(bclf,dataset,obs_fire,cv=kf)
print('All data:',np.mean(scores))  
"""predict for areas 
w/o evi, stemp: 0.9336099455049337
All data: 0.10774193548387097

w/0 wind,evi, stemp: 0.981557647644344
All data: 0.12419354838709677

w/o wind,evi, stemp, uwind: 0.9999999999999998
All data: 0.1338709677419355"""

"""predict for fireclass:
w/o wind,evi, stemp, uwind: 1.00000002
All data: 0.4963440860215054""""


  



