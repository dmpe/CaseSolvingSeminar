
class BaseTransformer(object):

    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self

    def transform(self, series):
        raise NotImplementedError()
        pass

