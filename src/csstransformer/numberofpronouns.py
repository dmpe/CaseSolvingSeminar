
from . import BaseTransformer

from . import TaggerFactory
from . import TokenizerFactory

class NumberOfPronouns(BaseTransformer):
    
    def __init__(self):
        pass

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            self._count_pronouns
        )
        return cpy

    def _count_pronouns(self, sentence):
        
        tagger = TaggerFactory.create().unigram()
        tokenizer = TokenizerFactory.create_word_punct()

        tokenized = tokenizer.tokenize(sentence)
        word_tags = tagger.tag(tokenized)

        pronouns = [
            word for word, tag in word_tags if tag and tag.count('PNP') > 0
        ]

        return len(pronouns)


