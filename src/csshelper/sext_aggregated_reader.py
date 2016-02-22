
from . import AggregatedReader

class SExtAggregatedReader(AggregatedReader):
    
    def __init__(self, sqlite_connection, determine_value=lambda x: int(x)):
        column = 'sExt'
        super(SExtAggregatedReader, self).__init__(sqlite_connection, column)
        self.determine_value = determine_value
        pass

    def _result_converter(self, result):
        return str(result[0]), self.determine_value(result[1])


