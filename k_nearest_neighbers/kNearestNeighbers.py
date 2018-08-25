import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

features_train, features_test, labels_train, labels_test = preprocess()


from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print "training time: " , round(time()-t0) , "s"

t1 = time()
pred = clf.predict(features_test)
print "training time: " , round(time()-t1) , "s"

from sklearn.metrics import accuracy_score
print(accuracy_score(pred, labels_test))