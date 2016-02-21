
from . import DataReader

class SAgrReader(DataReader):
    
    def __init__(self, sqlite_connection, determine_value=lambda x: int(x)):
        super(SAgrReader, self).__init__(sqlite_connection)
        self._header = ['sentence', 'sAgr']
        self.determine_value = determine_value
        pass

    def _get_query(self):
        return """
            SELECT
                [sentence]
                , [sAgr]
            FROM
                [Person] AS [p]
                INNER JOIN [Sentence] AS [s]
                    ON [p].[internal_id] = [s].[author]
            ;
        """
        pass

    def _result_converter(self, result):
        return str(result[0]), self.determine_value(result[1])


