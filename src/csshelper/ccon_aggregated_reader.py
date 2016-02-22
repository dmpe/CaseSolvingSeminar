
from . import AggregatedReader

class CConAggregatedReader(AggregatedReader):

    def __init__(self, sqlite_connection):
        column = 'cCon'
        super(CConAggregatedReader, self).__init__(sqlite_connection, column)
        pass

    def _result_converter(self, result):
        return str(result[0]), bool(result[1])

