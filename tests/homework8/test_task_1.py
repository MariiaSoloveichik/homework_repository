import pytest

from homework8.task1 import KeyValueStorage

storage = KeyValueStorage('task1.txt')

def test_1_key_value_storage_positive():
    """
    Testing that the attributes of the KeyValueStorage class contain keys and
    values available as collection elements and as attributes
    """
    assert storage.name == 'kek'
    assert storage.song == 'shadilay'
    assert storage.power == 9001


def test_2_key_value_storage_error():
    """Testing ValueError"""
    with pytest.raises(ValueError):
        assert KeyValueStorage('task1_2.txt')
