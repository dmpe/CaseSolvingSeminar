

from . import BaseTransformer

from . import TokenizerFactory

class AverageWordLength(BaseTransformer):

    def __init__(self):
        self.tokenizer = TokenizerFactory.create_word_only()
        pass

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            self._calculate_average_word_length
        )
        return cpy

    def _calculate_average_word_length(self, sentence):
        tokens = self.tokenizer.tokenize(sentence)

        count_of_words = len(tokens)

        if count_of_words > 0:
            return  sum([len(word) for word in tokens]) / count_of_words
        return 0



