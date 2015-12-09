
import sqlite3

class DataReader(object):

    def __init__(self, sqlite_connection):
        self.__sql_conn = sqlite_connection
        self.__cache = None
        pass

    def _get_query(self):
        raise NotImplementedError('must be implemented by heir')

    def _get_query_arguments(self):
        raise NotImplementedError('must be implemented by heir')

    def _result_converter(self, result_list):
        return tuple((r for r in result_list))

    def get_results(self):
        if not self.__cache:
            self.__cache = self.__get_results()
        return self.__cache
        pass

    def clear_cache(self):
        self.__cache = None

    def __get_results(self):
        query = self._get_query()
        query_args = self._get_query_arguments()
        cursor = self.__sql_conn.cursor()

        cursor.execute(query, query_args)

        result_list = []
        for result in cursor.fetchall():
            result_list.append(self._result_converter(result))
        return result_list



