# -*- coding: utf-8 -*-
"""project119.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ap6_S3dCYUXPWFNP46Si2N9hhYBkJUA
"""

import csv
import pandas as pd

col_name=['Passenger','Pclass','Sex','Age','SibSp','Parch','label']
df=pd.read_csv('project119.csv',names=col_name).iloc[1:]

df.head()

features=['Passenger','Pclass','Sex','Age','SibSp','Parch']

X=df[features]
y=df.label

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)

clf=DecisionTreeClassifier()
clf=clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

print('Accuracy : ',metrics.accuracy_score(y_test,y_pred))

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

dot_data=StringIO()

export_graphviz(clf,out_file=dot_data,filled=True,rounded=True,special_characters=True,
                feature_names=features,class_names=['0','1'])

#print(dot_data.getvalue())

import pydotplus

graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('Titanic.png')
Image(graph.create_png())

clf=DecisionTreeClassifier(max_depth=3)
clf=clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

print('Accuracy : ',metrics.accuracy_score(y_test,y_pred))

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

dot_data=StringIO()

export_graphviz(clf,out_file=dot_data,filled=True,rounded=True,special_characters=True,
                feature_names=features,class_names=['0','1'])

#print(dot_data.getvalue())
import pydotplus

graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('Titanic.png')
Image(graph.create_png())