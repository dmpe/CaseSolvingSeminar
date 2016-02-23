
import re

from . import BaseTransformer


class Smileys(object):

    smiley_regex = [
        re.compile('(:-?[\(\)])') # matches :) :( :-) :-(
        , re.compile('(D:|:D)') # matches :D D:
        , re.compile('(<3+)') # matches <3 <33 <333 ...
        , re.compile('(^[_.-]^)') # matches ^_^ ^-^ ^.^
    ]

    smileys = [
        ':)', ':(', ':-)', ':-(', 
        ':D', 'D:',
        '<3', '<33', '<333',
        '^_^', '^-^', '^.^'
    ]
    
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, series):
        cpy = series.copy()
        cpy = cpy.apply(
            self._extract_smileys
        )
        return cpy

    def _extract_smileys(self, sentence):

        found_smileys = [
            item 
            for r
            in SmileyTransformer.smiley_regex
                for item
                in r.findall(sentence)
        ]
        
        if not found_smileys:
            return ''

        return " ".join(found_smileys)


