
from . import DataReader

class AggregatedReader(DataReader):
    
    def __init__(self, sqlite_connection, column):
        super(AggregatedReader, self).__init__(sqlite_connection)
        self._header = ['sentence', column]
        pass

    def _get_query(self):
        return """
            SELECT
                group_concant([sentence])
                , [%s]
            FROM
                [Person] AS [p]
                INNER JOIN [Sentence] AS [s]
                    ON [p].[internal_id] = [s].[author]
            ;
        """ % column
        pass

    def _result_converter(self, result):
        return result


