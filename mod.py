import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib
import warnings
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import sklearn.preprocessing as pre

class predictor:
    sc_X = pre.StandardScaler()
    diabetes_data = pd.read_csv("./diabetes.csv")
    X =  pd.DataFrame(sc_X.fit_transform(diabetes_data.drop(["Outcome"],axis = 1),))
    y = diabetes_data.Outcome
    param_grid = {'n_neighbors':np.arange(1,50)}
    knn = KNeighborsClassifier()
    knn_cv= GridSearchCV(knn,param_grid,cv=5)
    knn_cv.fit(X,y)
    def predict(self,a):
        k=l=m=0
        #print(self.X.iloc[0])
        #mp = pd.DataFrame.from_records([a])
        son = pd.DataFrame(self.sc_X.transform([a]))
        #print(son)
        #input("k")
        """for t in range(0,500):
            a = self.X.iloc[t]
            #print(self.knn_cv.predict_proba([a]),self.knn_cv.predict([a]),self.y.iloc[t])
            #print(self.X.iloc[t])
            #prob = self.knn_cv.predict_proba([a])
            #input("wait")
            if prob[0][1]>0.50:
                res=1
            else:
                res=0
            if res==self.y.iloc[t]:
                l+=1
            else:
                m+=1
            k+=1
            #input("bekle")
        print(k,l,m)
        print(l/k)
        input("aa")"""
        return self.knn_cv.predict_proba(son)



