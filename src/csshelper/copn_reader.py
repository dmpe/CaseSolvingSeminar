
from . import DataReader

class COpnReader(DataReader):
    
    def __init__(self, sqlite_connection):
        super(COpnReader, self).__init__(sqlite_connection)
        self._header = ['sentence', 'cOpn']
        pass

    def _get_query(self):
        return """
            SELECT
                [sentence]
                , [cOpn]
            FROM
                [Person] AS [p]
                INNER JOIN [Sentence] AS [s]
                    ON [p].[internal_id] = [s].[author]
            ;
        """
        pass

    def _result_converter(self, result):
        return str(result[0]), bool(result[1])


