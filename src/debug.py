
import sqlite3
import csshelper
import pandas

c = sqlite3.connect('./data.sqlite3')

#r = csshelper.CNeuReader(c)
#cNeu_data = r.get_results()


import cssfeature

#sl_data = cssfeature.CharacterFeatures.string_length(cNeu_data, 0)

#import csstransformer

#pos_transformer = csstransformer.PartOfSpeech()
#ne_transformer = csstransformer.NounTransformer()

r = csshelper.SNeuReader(c)
r = csshelper.SNeuAggregatedReader(c)
sNeu_data = r.get_results()

import csstransformer
smiley = csstransformer.Smileys()

#ld = csstransformer.LexicalDiversity()





