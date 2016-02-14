
import sqlite3
import helper

c = sqlite3.connect('./data.sqlite3')

r = helper.CNeuReader(c)
result = r.get_results()



