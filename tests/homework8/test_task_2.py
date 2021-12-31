import os

from pytest import fixture

from homework8.task2 import TableData

DATABASE = os.path.join(os.path.dirname(__file__), 'example.sqlite')


@fixture
def presidents():
    """
    Create a SQLite database connection and close it
    when it's done.
    """
    presidents = TableData(database_name=DATABASE, table_name='presidents')
    try:
        yield presidents
    finally:
        presidents.close_con_to_bd()

def test_check_table_len(presidents):
    """
    Testing that method __len__ returns a correct length of
    specified tables from database.
    """
    assert len(presidents) == 3

def test_table_data_contains_return_bool(presidents):
    """
    Testing that method __contains__ returns a correct result if
    there are entries with the specified values in the tables.
    """
    assert 'Trump' in presidents
    assert "Yeltsin" in presidents
    assert 'Putin' not in presidents
