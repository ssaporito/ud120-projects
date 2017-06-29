#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score,recall_score

features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.3,random_state=42)

clf=DecisionTreeClassifier()
clf.fit(features_train,labels_train)
pred=clf.predict(features_test,labels_test)
print "pois:",reduce(lambda x,y:x+y,pred)
print "actual pois on test:",reduce(lambda x,y:x+y,labels_test)
true_positives=0
for i in range(0,len(pred)):
	true_positives+=pred[i]==labels_test[i] and pred[i]==1
print "true positives:",true_positives
print "total people:",len(features_test)
print "accuracy:",clf.score(features_test,labels_test)
print "precision:",precision_score(labels_test,pred)
print "recall:",recall_score(labels_test,pred)

