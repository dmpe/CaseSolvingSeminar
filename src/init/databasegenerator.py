
import pandas as pd

import sqlite3
import sys

class DatabaseManager(object):

    def __init__(self, db_path):
        self.__conn = sqlite3.connect(db_path)
        pass

    def close(self):
        self.__conn.commit()
        self.__conn.close()

    def create_tables(self):
        self.create_person_table()
        self.create_sentence_table()
        pass

    def store(self, row):
        if not self.has_person(row):
            self.insert_person(row)
        internal_id = self.get_person_id(row)
        self.insert_sentence(internal_id, row[1])

        #raise NotImplementedError()
        pass

    def has_person(self, row):
        external_id = row[0]
        cursor = self.__conn.cursor()
        cursor.execute('select 1 From Person Where external_id = :external_id'
            , {'external_id': external_id})
        return cursor.fetchone() is not None

    def get_person_id(self, row):
        external_id = row[0]
        cursor = self.__conn.cursor()
        cursor.execute('select internal_id From Person Where external_id = :external_id'
            , {'external_id': external_id})
        return cursor.fetchone()[0]

    def insert_person(self, row):
        """
        "#AUTHID", "STATUS"
        , "sEXT", "sNEU", "sAGR", "sCON", "sOPN"
        , "cEXT", "cNEU", "cAGR", "cCON", "cOPN"]]
        """
        cursor = self.__conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO
                Person
            VALUES
                (
                    null
                    , :external_id
                    , :sExt
                    , :sNeu
                    , :sAgr
                    , :sCon
                    , :sOpn
                    , :cExt
                    , :cNeu
                    , :cAgr
                    , :cCon
                    , :cOpn
                )
            ;
            """
            , {
                'external_id': row[0]
                , 'sExt': row[2]
                , 'sNeu': row[3]
                , 'sAgr': row[4]
                , 'sCon': row[5]
                , 'sOpn': row[6]
                , 'cExt': row[7]
                , 'cNeu': row[8]
                , 'cAgr': row[9]
                , 'cCon': row[10]
                , 'cOpn': row[11]
            })
        pass

    def insert_sentence(self, internal_id, sentence):
        cursor = self.__conn.cursor()
        cursor.execute("""
            INSERT INTO
                Sentence
            VALUES
                (
                    NULL
                    , :internal_id
                    , :sentence
                )
            ;
            """, {'internal_id': internal_id, 'sentence': sentence}
        )
        pass

    def create_person_table(self):
        cursor = self.__conn.cursor()
        statement = """
            CREATE TABLE IF NOT EXISTS Person (
                internal_id     INTEGER PRIMARY KEY
                , external_id   TEXT UNIQUE NOT NULL
                , sExt          REAL NOT NULL
                , sNeu          REAL NOT NULL
                , sAgr          REAL NOT NULL
                , sCon          REAL NOT NULL
                , sOpn          REAL NOT NULL
                , cExt          INTEGER NOT NULL
                , cNeu          INTEGER NOT NULL
                , cAgr          INTEGER NOT NULL
                , cCon          INTEGER NOT NULL
                , cOpn          INTEGER NOT NULL
            );
            """
        cursor.execute(statement)
        pass

    def create_sentence_table(self):
        cursor = self.__conn.cursor()
        statement = """
            CREATE TABLE IF NOT EXISTS Sentence (
                sentence_id     INTEGER PRIMARY KEY
                , author        INTEGER
                , sentence      TEXT

                , FOREIGN KEY (author) REFERENCES Person(internal_id)
            );
        """
        cursor.execute(statement)

def main(arg_list):

    data = arg_list[0]
    store_to = arg_list[1]

    dbhandler = DatabaseManager(store_to)
    dbhandler.create_tables()

    data = pd.read_csv("../raw_data/data.csv", parse_dates=True, infer_datetime_format=True,
        sep = None, encoding = "latin-1", engine = "python")

    rows = data[[
        "#AUTHID", "STATUS"
        , "sEXT", "sNEU", "sAGR", "sCON", "sOPN"
        , "cEXT", "cNEU", "cAGR", "cCON", "cOPN"]]

    for row in rows.values:
        row = (row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            , convert_string_to_boolean(row[7])
            , convert_string_to_boolean(row[8])
            , convert_string_to_boolean(row[9])
            , convert_string_to_boolean(row[10])
            , convert_string_to_boolean(row[11]))
        dbhandler.store(row)
    
    dbhandler.close()
    pass

def convert_string_to_boolean(string):
    positive_values = ['y', 'yes', '1']
    for pos in positive_values:
        if pos == string:
            return True
    return False

if __name__ == '__main__':
    main(sys.argv[1:])
