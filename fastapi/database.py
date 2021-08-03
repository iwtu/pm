from typing import Set
import psycopg2
import logging
from config import Settings


class Database:
    """PostgreSQL Database class."""

    def __init__(self, settings : Settings):
        self.connectionstring = settings.connectionstring        
        self.conn = None

    def open_connection(self):        
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(self.connectionstring)
            except psycopg2.DatabaseError as e:
                logging.error(e)
                raise e
            finally:
                logging.info('Connection opened successfully.')

    def select_row(self, query: str, val: tuple):        
        self.open_connection()
        with self.conn.cursor() as cur:
            cur.execute(query, val)
            record = cur.fetchone()
            cur.close()
            return record
    
    def select_rows(self, query:str, val: tuple):        
        self.open_connection()
        with self.conn.cursor() as cur:
            cur.execute(query, val)
            records = [row for row in cur.fetchall()]
            cur.close()
            return records

    def execute_query(self, query: str, val: tuple):        
        self.open_connection()
        with self.conn.cursor() as cur:
            cur.execute(query, val)
            self.conn.commit()            
            cur.close()
            return cur.rowcount
            

    