
from . import BaseTransformer

from . import TaggerFactory
from . import TokenizerFactory

class Nouns(BaseTransformer):
    
    def __init__(self):
        pass

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            self._extract_nouns
        )
        return cpy

    def _extract_nouns(self, sentence):
        
        tagger = TaggerFactory.create().unigram()
        tokenizer = TokenizerFactory.create_word_punct()

        tokenized = tokenizer.tokenize(sentence)
        word_tags = tagger.tag(tokenized)

        nouns = "".join(
            [ word for word, tag in word_tags if tag.count('NN') > 0]
        )

        return nouns



