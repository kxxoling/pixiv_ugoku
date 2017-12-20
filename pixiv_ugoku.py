# /usr/bin/env python
import os
import re
import json
import logging
import subprocess
from zipfile import ZipFile
from tempfile import mkstemp, mkdtemp

from six import text_type
import requests

headers = {'Referer': 'https://www.pixiv.net/'}
session = requests.Session()
session.trust_env = True
logger = logging.getLogger()

re_ugoku_illust_data = r'pixiv\.context\.ugokuIllustData\s+= ([^;]+)'


def get_html(url):
    logger.info('Fetching HTML from %s' % url)
    return session.get(url).content


def parse_html(html):
    ugoku_data = re.search(
        re_ugoku_illust_data, text_type(html)
    )
    assert ugoku_data
    logger.debug('Got data: ```%s```' % ugoku_data)
    ugoku_json = json.loads(ugoku_data.groups()[0])
    return ugoku_json


def download_zip(url):
    id_ = url.rsplit('/')[-1].rsplit('.')[0]
    tmp_dir = mkdtemp(prefix=str(id_))
    _, tmp_file = mkstemp(prefix=str(id_), dir=tmp_dir)

    logger.info('Saving zip to %s' % tmp_file)
    with open(tmp_file, 'wb') as f:
        for chunk in session.get(
            url, headers=headers
        ).iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    with ZipFile(tmp_file) as tar:
        for name in [i for i in tar.namelist() if i != 'index']:
            tar.extract(name, path=tmp_dir)
    return tmp_dir, tmp_file


def save_ugoku(url, filename='pixiv'):
    html = get_html(url)
    ugoku_json = parse_html(html)
    ugoku_zip = ugoku_json['src']
    dirname, _ = download_zip(ugoku_zip)
    fps = 1000 / 80

    subprocess.check_call(
        'ffmpeg -i "{dirname}/%6d.jpg" -y {output}'.format(
            fps=fps, dirname=dirname, output='%s.mp4' % filename
        ),
        shell=True
    )


def cli():
    import fire
    fire.Fire(save_ugoku)
