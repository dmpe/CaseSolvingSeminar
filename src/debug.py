
import sqlite3
import helper

c = sqlite3.connect('./data.sqlite3')

r = helper.CNeuReader(c)
data = r.get_results()


import cssfeature

sl_data = cssfeature.CharacterFeatures.string_length(data, 0)




