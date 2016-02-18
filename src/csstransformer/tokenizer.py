
import nltk
from nltk.tokenize import WordPunctTokenizer


class TokenizerFactory(object):
    

    class TokenizerImpl(object):
        
        def __init__(self):
            self.word_punct_tokenizer = WordPunctTokenizer()
            pass

        def word_punct(self):
            return self.word_punct_tokenizer

    __tokenizer_impl = TokenizerImpl()

    @staticmethod
    def create():
        return TokenizerFactory.__tokenizer_impl

