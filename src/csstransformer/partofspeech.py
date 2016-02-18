
import nltk
from .tagging import TaggerFactory
from .tokenizer import TokenizerFactory

import pdb

class PartOfSpeech(object):

    def __init__(self, ignore_unknown=False):
        self.ignore_unknown = ignore_unknown
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, series, col_name=None):
        cpy = series.copy()
        cpy  = cpy.apply(
            self._partofspeech
        )
        return cpy

    def _partofspeech(self, sentence):
        
        sentence = str(sentence)

        tagger = TaggerFactory.create().unigram()
        tokenizer = TokenizerFactory.create().word_punct()

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



