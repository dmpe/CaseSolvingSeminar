
from . import DataReader

class CNeuReader(DataReader):
    
    def __init__(self, sqlite_connection):
        super(CNeuReader, self).__init__(sqlite_connection)
        pass

    def _get_query(self):
        return """
            SELECT
                [sentence]
                , [cNeu]
                , RANDOM() as [rand]
            FROM
                [Person] AS [p]
                INNER JOIN [Sentence] AS [s]
                    ON [p].[internal_id] = [s].[author]
            ORDER BY
                [rand] ASC
            ;
        """
        pass

    def _result_converter(self, result):
        return result[0], bool(result[1])


