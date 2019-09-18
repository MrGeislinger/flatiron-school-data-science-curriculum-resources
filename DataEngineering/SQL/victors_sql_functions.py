import pandas as pd
import sqlite3

class VictorSql(object):
    
    def __init__(self, database=None):
        if database != None:
            self.conn = sqlite3.connect(database)
            self.cursor = self.conn.cursor()
            
    def get_tables(self):
        '''
        Return tables with a Pandas DataFrame from the connected database
        '''
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        return self.sql_to_df(query)

    def sql_with_cols(self, query, cursor=None):
        '''
        Gives me the full result (with columns)
        '''
        if cursor == None:
            cursor = self.cursor
            
        result = cursor.execute(query).fetchall()
        cols = tuple([description[0] for description in cursor.description])

        full_result = [cols] + result[:] 
        return full_result


    def sql_to_df(self, query, cursor=None):
        '''
        Create a DataFrame directly from a SQL query.
        '''
        if cursor == None:
            cursor = self.cursor
            
        results = self.sql_with_cols(query, cursor)
        return pd.DataFrame(columns=results[0], data=results[1:])


    def make_connection(self, database='data.sqlite'):
        '''
        A connection and cursor from a database
        '''
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

        

