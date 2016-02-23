

from . import BaseTransformer

class SentenceLength(BaseTransformer):

    def __init__(self):
        pass

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            self._calculate_length
        )
        return cpy

    def _calculate_length(self, sentence):
        return len(sentence)

