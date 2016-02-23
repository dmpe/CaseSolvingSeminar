

from . import BaseTransformer
from . import TokenizerFactory
from . import StemmerFactory

class LexicalDiversity(BaseTransformer):
    
    def __init__(self, stemmer=None):
        if stemmer:
            self.stemmer = stemmer
        else:
            self.stemmer = StemmerFactory.create_porter()
        self.tokenizer = TokenizerFactory.create_word_only()
        pass

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            self._calculate_lexical_diversity
        )
        return cpy

    def _calculate_lexical_diversity(self, sentence):
        stemmed_sentence = self.stemmer.stem(sentence)

        stemmed_tokens = self.tokenizer.tokenize(stemmed_sentence)
        tokenized_sentence = self.tokenizer.tokenize(sentence)

        unique_stems = set(stemmed_tokens)

        count_unique_stems = len(unique_stems)

        count_sentence_words = len(tokenized_sentence)

        if count_sentence_words > 0:
            lexical_diversity = count_unique_stems / count_sentence_words
        else:
            lexical_diversity = 0

        return lexical_diversity

