"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""


from typing import List
from collections import Counter, defaultdict
import string


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Returns a list of 10 longest words consisting from largest
    amount of unique symbols."""

    words_stat = defaultdict(list)

    with open(file_path, 'r', encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            words = line.split()
            for word in words:
                words_stat[len(word)].append(word.strip(string.punctuation))

    sorted_length = sorted(words_stat, reverse=True)
    answer = []

    for length in sorted_length:
        if not words_stat[length]:
            continue
        answer.append(words_stat[length].pop())
        if len(answer) > 9:
            break

    return answer


def get_rarest_char(file_path: str) -> str:
    """ Returns the number of rarest char in the document"""
    chars_stat = Counter()
    with open(file_path, 'r', encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for char in line:
                chars_stat[char] += 1

    return chars_stat.most_common()[-1][0]


def count_punctuation_chars(file_path: str) -> int:
    """ Returns the number of punctuation chars in the document"""

    counter = 0
    with open(file_path, 'r', encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for i in line:
                if 48 > ord(i) > 32:
                    counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    """ Returns the number of non_ascii_chars in the document"""

    ans = 0
    with open(file_path, 'r', encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for letter in line:
                if not letter.isascii():
                    ans += 1
    return ans


def get_most_common_non_ascii_char(file_path: str) -> str:
    """If there are no non-ascii characters in the file, SystemExit"""

    dict_letters = {}
    with open(file_path, 'r', encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for letter in line:
                if not letter.isascii():
                    if dict_letters.get(letter, -1) == -1:
                        dict_letters.update([(letter, 1)])
                    else:
                        dict_letters[letter] += 1

    major_count = max(dict_letters.values())
    for key in dict_letters.keys():
        if dict_letters[key] == major_count:
            return key
