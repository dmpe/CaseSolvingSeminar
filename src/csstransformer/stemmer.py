

import nltk

class StemmerFactory(object):

    @staticmethod
    def create_porter():
        return nltk.stem.PorterStemmer()

    @staticmethod
    def create_lancaster():
        return  nltk.stem.LancasterStemmer()
