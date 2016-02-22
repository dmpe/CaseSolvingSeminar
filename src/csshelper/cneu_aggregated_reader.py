
from . import AggregatedReader

class CNeuAggregatedReader(AggregatedReader):

    def __init__(self, sqlite_connection):
        column = 'cNeu'
        super(CNeuAggregatedReader, self).__init__(sqlite_connection, column)
        pass

    def _result_converter(self, result):
        return str(result[0]), bool(result[1])

