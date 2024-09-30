from unittest.mock import Mock, patch

from src.external_api import get_convert


def test_get_convert():
    mock_convert = Mock(return_value=1000)
    get_convert = mock_convert
    assert get_convert() == 1000
    mock_convert.assert_called_once_with()

@patch('requests.get')
def test_get_convert_2(mock_convert_2, transactions_dict):
    mock_convert_2.return_value.json.return_value = {'result':31957.58}
    assert get_convert(transactions_dict) == 31957.58

