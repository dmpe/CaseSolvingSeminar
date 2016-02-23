

import sklearn
import sklearn.base

class BaseTransformer(sklearn.base.BaseEstimator):

    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self

    def transform(self, series):
        raise NotImplementedError()
        pass

