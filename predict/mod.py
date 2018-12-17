import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
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
        son = pd.DataFrame(self.sc_X.transform([a]))
        arr = self.knn_cv.predict_proba(son)
        if arr[0] > 0.5:
            return [1, arr[0]]
        else:
            return [0, arr[0]]


