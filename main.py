import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')

data = pd.read_csv('./placement.csv')
print(data.head())
print(data.columns)

print(data.cgpa.describe()) #maximum cgpa is 8.5 and minimum cgpa is 3.3 and mean cgpa is 5.991

x = data.groupby(['cgpa'])['cgpa'].count()
print(x)
x1 = data['cgpa_range'] = pd.qcut(data['cgpa'], 4)

x2 = data.groupby(['cgpa_range'])['cgpa_range'].count()
# x3 = sns.countplot(x ='cgpa_range', data= data, alpha =0.7)
# plt.show()
print(x2) #most of the students had cgpa in the range 6-6.9
# x4 = data['iq_range'] = pd.qcut(data['iq'],)
print(data.iq.describe()) #max iq : 233.000000, min iq : 37, mean iq : 123.58
x4 = data['iq_range'] = pd.qcut(data['iq'],5)
x5 = data.groupby(['iq_range'])['iq_range'].count()
print(x5) #most of the students had iq range in between 37-90.

# f, ax= plt.subplots(1,2,figsize =(18,8))
# plt1 = sns.countplot(x= 'cgpa_range', data = data, hue = 'placement', ax = ax[0])
# plt2 = sns.countplot(x= 'iq_range', data = data, hue ='placement', ax =ax[1])
# plt.show()
#there is a high probability that a student will got placement if he/she has got good cgpa.
#but there is no guarantee that a student will get placement even if he/she has high iq.

# f, ax = plt.subplots(1,2,figsize=(18,8))
# sns.barplot(x='cgpa_range',y ='iq',data= data,ax =ax[0])
# sns.barplot(x='iq_range', y ='cgpa',data= data,ax = ax[1])
# plt.show()
#from the above observation, iq has no such relation on cgpa as well as on placement.

#if a student has high cgpa but low iq , will he/she get placement ?

print(np.where(data['cgpa']==8.5))
print(data[69:70])  #student who has highest cgpa ie 8.5 had iq 120, got placement.

data['cgpa_category']= 0
z1 = data.loc[(data['cgpa']>3.299)& (data['cgpa']<=5.075), 'cgpa_category']= 1
z2 = data.loc[(data['cgpa']>5.075)& (data['cgpa']<=6), 'cgpa_category']= 2
z3 = data.loc[(data['cgpa']>6)& (data['cgpa']<=6.9), 'cgpa_category']= 3
z4 = data.loc[(data['cgpa']>6.9)& (data['cgpa']<=8.5), 'cgpa_category']= 4

z5 = sns.countplot(x = 'iq_range', data= data[data['cgpa_category']==4],hue ='placement')
plt.show()
#Yes, there are so many students having high cgpa and low iq getting placements

#if a student has high iq but low cgpa, will he/she get placement?

print(np.where(data['iq']==233))
print(data[50:51]) #student with 233 iq has cgpa 3.5 ,no placement.

z6 = sns.countplot(x='cgpa_range', data=data[(data['iq']>154.2)&(data['iq']<=233)], hue ='placement')
plt.show()
#No, the student having high iq but low cgpa didn't get any placement.

plt4 = sns.countplot(x= 'cgpa_category', data= data, hue='placement')
plt.show()

data3 = np.array(data)
print(data3[50:51])


t1 = data.drop(['cgpa_range','cgpa_category','iq_range'],axis=1,inplace =True)
print(data.columns)
z11 = sns.heatmap(data.corr(), annot = True, cmap ='RdYlGn', linewidths = 0.2, annot_kws = {'size':20})
plt.show()