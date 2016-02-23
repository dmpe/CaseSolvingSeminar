

from . import BaseTransformer

class NumberOfCommas(BaseTransformer):

    def __init__(self):
        pass

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            lambda s: s.count(',')
        )
        return cpy


