
import nltk

from . import BaseTransformer
from . import TaggerFactory
from . import TokenizerFactory

class PartOfSpeech(BaseTransformer):

    def __init__(self, ignore_unknown=False):
        self.ignore_unknown = ignore_unknown
        pass

    def transform(self, series, col_name=None):
        cpy = series.copy()
        cpy  = cpy.apply(
            self._partofspeech
        )
        return cpy

    def _partofspeech(self, sentence):
        
        sentence = str(sentence)

        tagger = TaggerFactory.create().unigram()
        tokenizer = TokenizerFactory.create_word_punct()

        tokenised = tokenizer.tokenize(sentence)
        word_tags = tagger.tag(tokenised)

        if self.ignore_unknown:
            tags = " ".join(
                [ tag if tag else "" for word, tag in word_tags]
            )
        else:
            tags = " ".join(
                [ tag if tag else "None" for word, tag in word_tags]
            )
        
        return tags



