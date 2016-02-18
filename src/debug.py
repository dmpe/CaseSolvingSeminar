
import sqlite3
import helper
import pandas

c = sqlite3.connect('./data.sqlite3')

r = helper.CNeuReader(c)
data = r.get_results()


import cssfeature

#sl_data = cssfeature.CharacterFeatures.string_length(data, 0)

import csstransformer

t = csstransformer.PartOfSpeech()

pos = t.transform(data.sentence)
nor = data.sentence

df = pandas.DataFrame([pos, nor], columns=['pos', 'nor'])


