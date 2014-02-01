# simple tests
import justify


def test_line_width():
    text = 'Lorem ipsum dolor sit amet. consectetur adipiscing elit.'
    result = justify.justify(text, 60)
    line = result.split('\n')[0]
    assert len(line) == 60, 'Incorrect line width'


def test_justify():
    text = (
        'Fusce id tincidunt arcu. Pellentesque a '
        'leo laoreet quam varius convallis. '
        'Curabitur facilisis leo tortor, nec semper diam porta eu.')
    result = justify.justify(text, 40)
    line = result.split('\n')[-2]
    assert line[-1] != ' ', 'Justified error'


def test_indentation():
    text = 'Lorem ipsum'
    result = justify.justify(text, 60)
    assert result[0:4] == justify.TEXT_INDENT, 'No indentation'


def test_unicode():
    text = (
        'Якось кішка говорила:'
        '-- "Щось я, мабуть, захворіла!'
        'Чомусь нікуди не ходжу, '
        'Тільки все лежу й лежу.')
    result = justify.justify(text, 60)
    assert 'кішка' in result, 'Unicode error'
