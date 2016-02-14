
import sklearn
from sklearn import pipeline

from .classifiercollection import ClassifierCollection
from .extractorcollection import ExtractorCollection
from .selectorcollection import SelectorCollection

class PipeFactory(object):

    def __init__(self):
        self.classifiers = ClassifierCollection()
        self.extractors = ExtractorCollection()
        self.selectors = SelectorCollection()
        pass

    def create_tfidf_nb(self):
        pipe = sklearn.pipeline.Pipeline([
            self.extractors.tfidf_vectorizer
            , self.selectors.select_k_best
            , self.classifiers.multinomial_nb
        ])
        return pipe
    
    
