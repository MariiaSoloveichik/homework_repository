import pytest

from homework4.task_2 import count_dots_on_i


def test_count_dots_on_i_correct_answer():
    assert count_dots_on_i('https://example.com/') == 59


def test_count_dots_on_i_wrong_url():
    with pytest.raises(ValueError):
        count_dots_on_i('https://pryanikc.pryanikc/')
