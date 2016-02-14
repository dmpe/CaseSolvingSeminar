
from . import DataReader

class CNeuReader(DataReader):
    
    def __init__(self, sqlite_connection):
        super(CNeuReader, self).__init__(sqlite_connection)
        self._header = ['sentence', 'cNeu']
        pass

    def _get_query(self):
        return """
            SELECT
                [sentence]
                , [cNeu]
            FROM
                [Person] AS [p]
                INNER JOIN [Sentence] AS [s]
                    ON [p].[internal_id] = [s].[author]
            ORDER BY
                RANDOM()
            ;
        """
        pass

    def _result_converter(self, result):
        return result[0], bool(result[1])


