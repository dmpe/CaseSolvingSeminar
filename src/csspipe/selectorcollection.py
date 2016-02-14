
import sklearn
from sklearn import feature_selection

class SelectorCollection(object):
    
    def __init__(self):
        self._init_feature_selection()
        pass

    def _init_feature_selection(self):
        self.select_k_best = (
            'chi2'
            , sklearn.feature_selection.SelectKBest(
                sklearn.feature_selection.chi2
                , k=1000))
        pass





