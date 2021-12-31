"""
Homework 2:
Preamble
We have a database file (example.sqlite) in sqlite3 format with some tables
and data. All tables have 'name' column and maybe some additional ones.
Data retrieval and modifications are done with sqlite3 module by issuing SQL
statements. For example, to get all data from TABLE1:
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('SELECT * from TABLE1')
data = cursor.fetchall()   # will be a list with data.
instead of getting all data at once, you can use .fetchone() calls and named
expressions:
while row:=cursor.fetchone():
    print(row)
To get a row with specific name equal to some value:
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('SELECT * from presidents where name=:name', {name:'Yeltsin'})
data = cursor.fetchall()  # will get all records with this name. You can also
use .fetchone() to get one record.
in order to get record with first name (sorted alphabetically) use SQL
expression SELECT * from presidents order by name asc limit 1 in order to get
record after specified (sorted alphabetically) use SQL expression
SELECT * from presidents where name > :name order by name limit. To get
amount of records in table TABLE1, use select count(*) from TABLE1 query.
Please refer to this documents for more information about how to retrieve
data from sqlite database:
DBAPI: https://www.python.org/dev/peps/pep-0249/
sqlite3 module: https://docs.python.org/3/library/sqlite3.html
Task
Write a wrapper class TableData for database table, that when initialized
with database name and table acts as collection object
(implements Collection protocol).
Assume all data has unique values in 'name' column. So, if
presidents = TableData(database_name='example.sqlite', table_name='presidents')
then
len(presidents) will give current amount of rows in presidents table in
database presidents['Yeltsin'] should return single data row for president
with name Yeltsin 'Yeltsin' in presidents should return if president with
same name exists in table object implements iteration protocol. i.e. you could
use it in for loops::
for president in presidents:
print(president['name'])
all above mentioned calls should reflect most recent data. If data in table
changed after you created collection instance, your calls should return
updated data.
Avoid reading entire table into memory. When iterating through records, start
reading the first record, then go to the next one, until records are exhausted.
When writing tests, it's not always necessary to mock database calls
completely. Use supplied example.sqlite file as database fixture file
"""

import sqlite3
from typing import Tuple


class TableData:
    """
    Class initializes with database name and table as collection object
    """

    def __init__(self, database_name, table_name) -> None:
        """
        Method to initialize the object’s attributes
        :param database_name: string, database file
        :param table_name: string, table name
        """
        self.database = database_name
        self.table = table_name
        self.con = sqlite3.connect(self.database)
        self.cursor = self.con.cursor()

    def bd_connect(self):
        """
        Method make a database connection
        """
        self.con = sqlite3.connect(self.database)
        self.cursor = self.con.cursor()

    def close_con_to_bd(self):
        """
        The method confirms that the connection to the database is closed.
        """
        self.cursor.close()
        self.con.close()

    def __len__(self):
        """
        Method returns the length, the number of rows in a table.
        :return: int, the number of rows in a table
        """
        self.cursor.execute(f'SELECT count(*) FROM {self.table}')
        return self.cursor.fetchone()[0]

    def __contains__(self, item):
        """
        Method checks that table contains a specified name
        :param item: str, the value to be checked
        :return: True if there is an entry in the table, otherwise False
        """
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE name='{item}'")
        return bool(self.cursor.fetchone())

    def __iter__(self) -> Tuple:
        """
        Initializes an iterator protocol for the table.
        :return: tuple, contain rows of the table
        """
        yield from self.cursor.execute(f"SELECT * FROM {self.table}")


if __name__ == '__main__':
    presidents = TableData(database_name='example.sqlite', table_name='presidents')
    print(len(presidents))
    for president in presidents:
        print(president["name"])
