from sklearn import svm
import numpy as np

class SVMModel:
    def __init__(self):
        self.model = svm.SVC(kernel='linear')

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def get_params(self):
        w = self.model.coef_[0]
        b = self.model.intercept_[0]
        return w, b