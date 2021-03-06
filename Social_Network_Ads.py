
import pandas as pd
import numpy as np

df=pd.read_csv('/content/Social_Network_Ads.csv')

df=df.drop(columns='User ID')
df.head()

df.describe()

df.info()

hassan=df['Age'].value_counts()
hassan.plot.hist();

khalid=df['Gender'].value_counts()
khalid.plot.pie(subplots=True,autopct='%1.1f%%');

aziz=df['Purchased'].value_counts()
aziz.plot.pie(subplots=True,autopct='%1.1f%%');

import matplotlib.pyplot as plt

# scatterplot
colors = ['orange', 'purple']
purchased = [0,1]

for i in range(2):
    x = df[df['Purchased'] == purchased[i]]
    plt.scatter(x['Age'], x['EstimatedSalary'], c = colors[i], label=purchased[i])
plt.xlabel("Age")
plt.ylabel("EstimatedSalary")
plt.legend();

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])
df.head()

for i in range(2):
    x = df[df['Purchased'] == purchased[i]]
    plt.scatter(x['Age'], x['Gender'], c = colors[i], label=purchased[i])
plt.xlabel("Age")
plt.ylabel("Gender")
plt.legend();

X=df.iloc[:,:-1]
y=df['Purchased']

print('inputs shape:',X.shape)
print('outputs shape:',y.shape)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier

error_rate = []

for i in range(1,40):
    knn = KNeighborsClassifier( n_neighbors = i)
    knn.fit(X_train , y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure( figsize=(10,8))
plt.plot( range(1,40) , error_rate , color='purple', linestyle='--', marker='o',
         markerfacecolor='yellow', markersize=10);

nnn=error_rate.index(min(error_rate))+1
print('the best number of neighbors is:',nnn)

knn=KNeighborsClassifier(n_neighbors=nnn)
knn.fit(X_train,y_train)

print('knn score is:',knn.score(X_test,y_test)*100,'%')
