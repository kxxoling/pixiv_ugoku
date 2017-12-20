try:
    import mock                 # PY2
except ImportError:
    from unittest import mock   # PY3

from fire import Fire
from fire.core import FireExit

import pixiv_ugoku
from pixiv_ugoku import save_ugoku

def test_cli_args(mocker):
    some_pixiv_url = 'https://pixiv.net/some_url'
    custom_filename = 'custom_filename'
    mocker.patch('sys.argv', ['ugoku', some_pixiv_url, '--filename', custom_filename])
    mocked = mocker.patch.object(pixiv_ugoku, 'save_ugoku', autospec=True)
    try:
        Fire(mocked)
    except FireExit:
        pass
    mocked.assert_called_once_with(some_pixiv_url, filename=custom_filename)
