
#Usage of DataReader

In order to utilize the database one can create a child of the abstract class DataReader.
An example is given in TestReader.
One only has to provide a sql-query (plus parameter).
Afterwards one can query the results by calling *get_results* on the TestReader instance.

*Do not forget to insert your class in __init__.py*

#Example

import sqlite3

import helper

con = sqlite3.connect('../data.sqlite3')

tr = TestReader(con)

results = tr.get\_results()

print(results[0])






