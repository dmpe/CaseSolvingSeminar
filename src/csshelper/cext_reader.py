
from . import DataReader

class CExtReader(DataReader):
    
    def __init__(self, sqlite_connection):
        super(CExtReader, self).__init__(sqlite_connection)
        self._header = ['sentence', 'cExt']
        pass

    def _get_query(self):
        return """
            SELECT
                [sentence]
                , [cExt]
            FROM
                [Person] AS [p]
                INNER JOIN [Sentence] AS [s]
                    ON [p].[internal_id] = [s].[author]
            ;
        """
        pass

    def _result_converter(self, result):
        return str(result[0]), bool(result[1])


