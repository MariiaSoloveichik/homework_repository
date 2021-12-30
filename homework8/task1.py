"""
Homework 1:
We have a file that works as key-value storage, each line is represented as key
and value separated by = symbol, example:
name=kek last_name=top song_name=shadilay power=9001
Values can be strings or integer numbers. If a value can be treated both as a
number and a string, it is treated as number.
Write a wrapper class for this key value storage that works like this:
storage = KeyValueStorage('path_to_file.txt') that has its keys and values
accessible as collection items and as attributes. Example: storage['name']
# will be string 'kek' storage.song_name # will be 'shadilay' storage.power
# will be integer 9001
In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when
there's a line 1=something) ValueError should be raised. File size is expected
to be small, you are permitted to read it entirely into memory.
"""
from collections import defaultdict


class KeyValueStorage:
    """ Class for saving attributes from a file. """
    def __init__(self, file) -> None:
        """
        Method to initialize the object’s attributes
        :param file: path to a file that is a key value storage file.
        """
        self.custom_dict = defaultdict(str)
        with open(file, 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                if value.lstrip('-').isnumeric():
                    value = int(value)
                if key.lstrip('-').isdigit():
                    raise ValueError("Incorrect type of key value")
                if not hasattr(KeyValueStorage, key):
                    setattr(self, key, value)
                    self.custom_dict[key] = value

    def __getitem__(self, key):
        """
        Getting a value whose key is available as a collection item.
        :param key: the key whose value should be returned
        :return: the value defined for the key
        """
        return self.custom_dict[key]
