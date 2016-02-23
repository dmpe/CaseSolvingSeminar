
from . import BaseTransformer

from . import TaggerFactory
from . import TokenizerFactory
from . import FunctionalWordsIdentifierFactory

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

        [x for x in y]

        count_list = [
            True for t in tokens if self.fw_identifier.is_functional_word(t)
        ]

        return len(count_list)


