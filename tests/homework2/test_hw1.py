from homework2.hw2_task_1 import (count_non_ascii_chars,
                                  count_punctuation_chars,
                                  get_longest_diverse_words,
                                  get_most_common_non_ascii_char,
                                  get_rarest_char)


def test_get_longest_diverse_words():
    """ Check how works this function and what longest
    diverse words"""
    assert get_longest_diverse_words("data.txt") == [
        'Verfassungsverletzungen',
        'Entscheidungsschlacht',
        'politisch-technischen',
        'Millionenbevölkerung',
        'Nachrichtenmitteln',
        'Staatsrechtslehrer',
        'materialistischen',
        'veranschaulichen',
        'Schutzumschlag',
        'Aufzeichnungen']


def test_get_rarest_char():
    """ Check how works this function and what
     the rarest_char"""
    assert get_rarest_char("data.txt") == ')'


def test_count_punctuation_chars():
    """ Check how works this function and how much
     punctuation chars"""
    assert count_punctuation_chars("data.txt") == 5125


def test_count_non_ascii_chars():
    """ Check how works this function and how much
    non ascii chars"""
    assert count_non_ascii_chars("data.txt") == 2971


def test_get_most_common_non_ascii_char():
    """ Check how works this function and how much
    non ascii chars"""
    assert get_most_common_non_ascii_char("data.txt") == 'ä'
