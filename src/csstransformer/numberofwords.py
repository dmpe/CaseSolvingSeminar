

from . import BaseTransformer
from . import TokenizerFactory

class NumberOfWords(BaseTransformer):

    def __init__(self):
        self.tokenizer = TokenizerFactory.create_word_only()
        pass

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            lambda s: len(self.tokenizer.tokenize(s))
        )
        return cpy


