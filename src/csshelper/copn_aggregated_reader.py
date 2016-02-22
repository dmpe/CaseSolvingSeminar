
from . import AggregatedReader

class COpnAggregatedReader(AggregatedReader):

    def __init__(self, sqlite_connection):
        column = 'cOpn'
        super(COpnAggregatedReader, self).__init__(sqlite_connection, column)
        pass

    def _result_converter(self, result):
        return str(result[0]), bool(result[1])

