

from . import BaseTransformer

class NumberOfDotsTransformer(BaseTransformer):

    def __init__(self):
        pass

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            self._calculate_number_of_dots
        )
        return cpy

    def _calculate_number_of_dots(self, sentence):
        return sentence.count('.')


