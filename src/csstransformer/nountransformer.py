
from .tagging import TaggerFactory
from .tokenizer import TokenizerFactory

class NounTransformer(object):
    
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            self._extract_nouns
        )
        return cpy
        pass

    def _extract_nouns(self, sentence):
        
        tagger = TaggerFactory.create().unigram()
        tokenizer = TokenizerFactory.create().word_punct()

        tokenized = tokenizer.tokenize(sentence)
        word_tags = tagger.tag(tokenized)

        nouns = "".join(
            [ word if tag == 'NN' else '' for word, tag in word_tags]
        )
        return nouns



