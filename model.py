import sqlite3
from sqlite3 import Error

class Library:
    def__init__(self,Name ='Byte')
       self.Name=Name
       
    def connect(self):
        self.connection=sqlite3.connect('LibraryDatabase.db')
        self.cursor=self.connection.cursor()
    def create_tables(self)
    try.self.cursor.execute(
        '''create table if not exists librarian (nametext,emailtext,passwordtext,phone_numberinteger)'''
    )