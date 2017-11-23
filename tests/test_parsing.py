import os
import re
import json

from pixiv_ugoku import re_ugoku_illust_data
from pixiv_ugoku import parse_html

TESTS_PATH = os.path.dirname(os.path.abspath(__file__))

pixiv_html_path = os.path.join(TESTS_PATH, 'data', 'pixiv_illust_47594886.html')
with open(pixiv_html_path) as f:
    fixture = f.read()


def test_re_ugoku_illust_data():
    result = re.search(re_ugoku_illust_data, fixture)
    assert result
    ugoku_json = json.loads(result.groups()[0])
    assert ugoku_json


def test_parse_html():
    ugoku_json = parse_html(fixture)
    assert ugoku_json['src'] == 'https://i.pximg.net/img-zip-ugoira/img/2014/12/17/00/06/04/47594886_ugoira600x600.zip'
