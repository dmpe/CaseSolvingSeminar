import pandas as pd
import numpy as np
from numpy import *
import re, reprlib, sys 
from itertools import *
import random as ran
ran.seed(5125)

import sklearn as sk
from sklearn import *
from sklearn.feature_extraction.text import *
from sklearn.svm import *
from sklearn.cross_validation import *
from sklearn.pipeline import *
from sklearn.multiclass import *
from sklearn.datasets import *
from sklearn.naive_bayes import *
from sklearn.neighbors import *
from sklearn.cluster import *
from sklearn.feature_selection import *
from sklearn.ensemble import *
from sklearn.linear_model import *
from sklearn.tree import *
from sklearn.grid_search import *
from sklearn.base import *
from sklearn.datasets.twenty_newsgroups import *
from sklearn.decomposition import *
from sklearn.feature_extraction import *
from sklearn.metrics import *

class ColumnAll(object):
    def fit(self, x, y=None):
        return self

    def transform(self, x):
        print("debug Col-Selec ALL")
        data_all = x.iloc[:, :]
        return data_all

class ColumnSelector(object):
    def fit(self, x, y=None):
        return self

    def transform(self, x):
        string_col = x.iloc[:, 0]
        print("debug Col-Selec (STATUS only)")
        print(string_col.shape)
        return string_col
    
class ColumnExtractor(object):
    def transform(self, x):
        cols = x.iloc[:, 1:]
        print("debug Col-Extrac (Rest)")
        print(cols.shape)
        return cols

    def fit(self, x, y=None):
        return self
    
class ModelTransformer(TransformerMixin):
    def __init__(self, model):
        self.model = model

    def fit(self, *args, **kwargs):
        self.model.fit(*args, **kwargs)
        return self

    def transform(self, x, **transform_params):
        return pd.DataFrame(self.model.predict(x))

class DenseTransformer(object):
    """Convert a sparse matrix into a dense matrix."""
    def __init__(self, some_param=True):
        pass

    def transform(self, x, y=None):
        return x.toarray()

    def fit(self, x, y=None):
        return self

    def fit_transform(self, x, y=None):
        return x.toarray()

    def get_params(self, deep=True):
        return {'some_param': True}
