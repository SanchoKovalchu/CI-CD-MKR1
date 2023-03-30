import os
import sys
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solution import clean_text, find_top_10_words, read_file, split_into_words


@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'test.txt')
    with open(target_file, 'w') as file:
        lines = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n',
                 'Fusce eu commodo arcu. Phasellus imperdiet convallis turpis.\n'
                 ]
        file.writelines(lines)

    return target_file

@pytest.mark.parametrize("text, expected_output", [([], []),
                                                   (["", "", ""], ["", "", ""]),
                                                   (["hello\n", "world\n"], ["hello", "world"])])
def test_clean_text(text, expected_output):
    assert clean_text(text) == expected_output

@pytest.mark.parametrize('words, expected_output', [([], []),
                                                    (["hello world"], ["hello", "world"]),
                                                    (["hello world", "this is a sample text. hello?"], 
                                                     ["hello", "world", "this", "is", "a", "sample", "text", "hello"])])
def test_split_into_words(words, expected_output):
    assert split_into_words(words) == expected_output


@pytest.mark.parametrize("words, expected_output", [([], []),
                                                    (["hello", "world", "hello", "world"], [("hello", 2), ("world", 2)]),
                                                    (["hello","world","this","is","a","sample","text","hello","world","hello","world","sample", "sample","text"], 
                                                     [("hello", 3),("world", 3),("sample", 3),("text", 2),("this", 1),("is", 1),("a", 1)])])
def test_find_top_10_words(words, expected_output):
    # Test empty list
    assert find_top_10_words(words) == expected_output


@pytest.mark.parametrize("expected_output", 
                         [['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
                           'Fusce eu commodo arcu. Phasellus imperdiet convallis turpis.']])
def test_read_file(prepare_text_file, expected_output):
    # Test reading an existing file
    assert read_file(prepare_text_file) == expected_output
