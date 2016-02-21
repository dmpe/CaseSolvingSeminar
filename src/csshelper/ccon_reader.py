
from . import DataReader

class CConReader(DataReader):
    
    def __init__(self, sqlite_connection):
        super(CConReader, self).__init__(sqlite_connection)
        self._header = ['sentence', 'cCon']
        pass

    def _get_query(self):
        return """
            SELECT
                [sentence]
                , [cCon]
            FROM
                [Person] AS [p]
                INNER JOIN [Sentence] AS [s]
                    ON [p].[internal_id] = [s].[author]
            ;
        """
        pass

    def _result_converter(self, result):
        return str(result[0]), bool(result[1])


