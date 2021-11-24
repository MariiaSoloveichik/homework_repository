from unittest.mock import patch

import pytest

from homework4.task_2 import count_dots_on_i


def test_count_dots_on_i_correct_answer():
    assert count_dots_on_i('https://example.com/') == 59


def test_count_dots_on_i_wrong_url():
    with pytest.raises(ValueError):
        count_dots_on_i('https://pryanikc.pryanikc/')


def test_count_dots_on_i_with_mock_correct_answer():
    path_for_mock = 'homework4.task_2.get_html_from_url'
    with patch(target=path_for_mock, return_value='iiii'):
        assert count_dots_on_i('https://example.com/') == 4
