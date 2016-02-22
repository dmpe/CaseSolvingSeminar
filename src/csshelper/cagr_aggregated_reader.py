
from . import AggregatedReader

class CAgrAggregatedReader(AggregatedReader):

    def __init__(self, sqlite_connection):
        column = 'cAgr'
        super(CAgrAggregatedReader, self).__init__(sqlite_connection, column)
        pass

    def _result_converter(self, result):
        return str(result[0]), bool(result[1])

