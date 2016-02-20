
import pdb

import numpy
import pandas
import sqlite3

from pandas.core.frame import DataFrame

class DataReader(object):

    def __init__(self, sqlite_connection):
        self.__sql_conn = sqlite_connection
        self.__cache = None
        self._header = None
        pass

    def _get_query(self):
        raise NotImplementedError('must be implemented by heir')

    def _get_query_arguments(self):
        return {}

    def _result_converter(self, result):
        return result

    def get_results(self):
        query = self._get_query()
        query_args = self._get_query_arguments()
        cursor = self.__sql_conn.cursor()

        cursor.execute(query, query_args)
        iterable_data = cursor.fetchall()
        return self._create_output(iterable_data)

    def _create_output(self, iterable_data):

        matrix = DataFrame(
            [self._result_converter(data) for data in iterable_data]
            , columns=self._header
        )

        return matrix

