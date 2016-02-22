
import nltk

from nltk.corpus import treebank
from nltk.tag import UnigramTagger

class TaggerFactory(object):

    class TaggerImpl(object):
    
        def __init__(self):
            train_sents = treebank.tagged_sents()
            self.unigram_tagger = UnigramTagger(train_sents)
            pass

        def unigram(self):
            return self.unigram_tagger

    __tagger_impl = TaggerImpl()

    @staticmethod
    def create():
        return TaggerFactory.__tagger_impl
        pass




