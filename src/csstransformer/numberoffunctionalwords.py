
from . import BaseTransformer

from . import TaggerFactory
from . import TokenizerFactory
form . import FunctionalWordsIdentifierFactory

class NumberOfFunctionalWords(BaseTransformer):
    
    def __init__(self):
        self.fw_identifier = FunctionalWordsIdentifierFactory.create()
        pass

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            self._count_pronouns
        )
        return cpy

    def _count_pronouns(self, sentence):
        
        tokenizer = TokenizerFactory.create_word_punct()

        tokens = tokenizer.tokenize(sentence)

        count_list = [
            True if self.fw_identifier.is_functional_word(t)
            for t in tokens
        ]

        return len(count_list)


