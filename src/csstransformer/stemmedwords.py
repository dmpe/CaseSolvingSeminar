
from . import StemmerFactory
from . import BaseTransformer

class StemmedWordsTransformer(BaseTransformer):
    
    def __init__(self, stemmer=None):
        if stemmer:
            self.stemmer = stemmer
        else:
            self.stemmer = StemmerFactory.create_porter()
        pass

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            self._stem_words
        )
        return cpy
    

    def _stem_words(self, sentence):
        return self.stemmer.stem(sentence)

