
import pandas

import sklearn
import sklearn.base

class Aggregator(sklearn.base.BaseEstimator):

    def __init__(self, transformers):
        self.transformers = transformers
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, series):
        tseries = [ t.transform(series) for t in self.transformers ]
        df = pandas.concat(objs=tseries, axis=1)
        return df


