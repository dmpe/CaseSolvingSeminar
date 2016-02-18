
import nltk
from .tagging import TaggerFactory
from .tokenizer import TokenizerFactory

import pdb

class PartOfSpeech(object):

    def __init__(self, column):
        self.column = column
        pass


    def fit(self, X, y=None):
        return self

    def transform(self, dataframe, col_name=None):
        cpy = dataframe.copy()
        cpy  = cpy.apply(
            self._partofspeech
            , axis='columns'
            , raw=True
        )
        return cpy

    def _partofspeech(self, row):

        item_pos = (self.column, )
        sentence = row.item(item_pos)

        tagger = TaggerFactory.create().unigram()
        tokenizer = TokenizerFactory.create().word_punct()

        tokenised = tokenizer.tokenize(sentence)
        word_tags = tagger.tag(tokenised)

        #tags_list = [ x for x in map(lambda wt: wt[1], word_tags)]

        tags = " ".join(
            [ tag if tag else "None" for word, tag in word_tags]
        )

        row.itemset(item_pos, tags)
        
        return row



