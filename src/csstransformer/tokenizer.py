
import nltk
from nltk.tokenize import WordPunctTokenizer

class TokenizerFactory(object):
    
    __word_punct_tokenizer_impl = nltk.tokenize.WordPunctTokenizer()
    __word_only_tokenizer_impl = nltk.tokenize.RegexpTokenizer('\w+')


    @staticmethod
    def create(tokenizer):
        if tokenizer == 'word_punct':
            return TokenizerFactory.create_word_punct()
        if tokenizer == 'word_only':
            return TokenizerFactory.create_word_only()

    @staticmethod
    def create_word_punct():
        return TokenizerFactory.__word_punct_tokenizer_impl
    
    @staticmethod
    def create_word_only():
        return TokenizerFactory.__word_only_tokenizer_impl

