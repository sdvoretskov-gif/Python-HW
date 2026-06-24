import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize(
    'input_text, expected_output',
    [
        ('Hello', 'Hello'), ('world', 'World'),
        ('hello world', 'Hello world'),
    ]
)
def test_upper_letter_positive(input_text, expected_output):
    assert string_utils.capitalize(input_text) == expected_output


@pytest.mark.parametrize(
    'input_text, expected_output',
    [
        ('123', '123'), (' world', 'World'), ('привет', 'Привет'),
    ]
)
def test_upper_letter_negative(input_text, expected_output):
    assert string_utils.capitalize(input_text) == expected_output


@pytest.mark.parametrize(
    'input_text, expected_output',
    [
        (' Hello', 'Hello'), (' ', ''),
        ('  hello world', 'hello world'),
    ]
)
def test_whitespace_positive(input_text, expected_output):
    assert string_utils.trim(input_text) == expected_output


@pytest.mark.parametrize(
    'input_text, expected_output',
    [
        ('_ Hello', 'Hello'), (' . Hello', '.Hello'),
        ('12  hello world', 'hello world'),
    ]
)
def test_whitespace_negative(input_text, expected_output):
    assert string_utils.trim(input_text) == expected_output


@pytest.mark.parametrize(
    'input_text, input_symbol',
    [
        ('Hello', 'H'), ('123', '2'),
        ('hello_world', '_'),
    ]
)
def test_symbol_positive(input_text, input_symbol):
    assert string_utils.contains(input_text, input_symbol) is True


@pytest.mark.parametrize(
    'input_text, input_symbol',
    [
        ('Hello', 't'), ('hello1', '2'),
        (' hello_world', ' '),
    ]
)
def test_symbol_negative(input_text, input_symbol):
    assert string_utils.contains(input_text, input_symbol) is True


@pytest.mark.parametrize(
    'input_text, input_del_text',
    [
        ('Hello', 'H'), ('123', '2'),
        ('hello_world', '_'),
    ]
)
def test_delete_symbol_positive(input_text, input_del_text):
    assert string_utils.delete_symbol(input_text, input_del_text) != input_text


@pytest.mark.parametrize(
    'input_text, input_del_text',
    [
        ('Hello', 'v'), ('123', ' '),
        ('hello_world', 'H'),
    ]
)
def test_delete_symbol_negative(input_text, input_del_text):
    assert string_utils.delete_symbol(input_text, input_del_text) != input_text
