import pytest
from string_processor import StringProcessor

processor = StringProcessor()

@pytest.mark.parametrize(
    'input_text, expected_output',
    [
    ('Hello', 'Hello.'), ('hello', 'Hello.'), ('Hello world', 'Hello world.'),
    ]
)
def test_proces_positive(input_text, expected_output):
    assert processor.process(input_text) == expected_output

@pytest.mark.parametrize(
    'input_text, expected_output',
    [
    ('', '.'), ('    ', '    .',)
    ]
)
def test_proces_negative(input_text, expected_output):
    assert processor.process(input_text) == expected_output

