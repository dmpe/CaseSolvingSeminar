
from . import DataReader

class TestReader(DataReader):

    def __init__(self, sqlite_connection):
        super(TestReader, self).__init__(sqlite_connection)
        pass

    def _get_query(self):
        return """
            SELECT
                external_id
                , sentence
                , sExt
                , cExt
            FROM
                Person AS p
                INNER JOIN Sentence AS s
                    ON p.internal_id = s.author
            WHERE
                cExt = :cExt_val
            ;

        """

    def _get_query_arguments(self):
        return {'cExt_val': False}

