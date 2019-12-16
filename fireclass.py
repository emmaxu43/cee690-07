import numpy as np
import pandas as pd

file= "/home/cx43/cee690-07/data/2018fire/test2_fire.csv"
dataset= pd.read_csv(file)
df = pd.DataFrame(dataset)

tmp= np.array(df['burnedarea'])
#class A=1, class G= 7
m1= tmp<= 0.25
tmp[m1]=1

m2= (tmp> 0.25) & (tmp<10)
tmp[m2]=2

m3= (tmp>= 10) & (tmp<100)
tmp[m3]=3

m4= (tmp>= 100) & (tmp<300)
tmp[m4]=4

m5= (tmp>= 300) & (tmp<1000)
tmp[m5]=5

m6= (tmp>= 1000) & (tmp<5000)
tmp[m6]= 6

m7= tmp> 5000
tmp[m7]=7

df['fireClass'] = tmp
df.to_csv(file)