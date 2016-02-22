
from . import AggregatedReader

class CExtAggregatedReader(AggregatedReader):

    def __init__(self, sqlite_connection):
        column = 'cExt'
        super(CExtAggregatedReader, self).__init__(sqlite_connection, column)
        pass

    def _result_converter(self, result):
        return str(result[0]), bool(result[1])

