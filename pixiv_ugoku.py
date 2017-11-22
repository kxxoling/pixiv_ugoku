# /usr/bin/env python
import os
import re
import json
import subprocess
from zipfile import ZipFile

import requests

headers = {'Referer': 'https://www.pixiv.net/'}
session = requests.Session()
session.trust_env = True


def get_html(url):
    return session.get(url).content


def parse_html(html):
    ugoku_data = re.search(
        r'pixiv\.context\.ugokuIllustData\s+= ([^;]+)', html.decode('utf-8')
    )
    assert ugoku_data
    ugoku_json = json.loads(ugoku_data.groups()[0])
    return ugoku_json


def download_zip(url):
    id_ = url.rsplit('/')[-1].rsplit('.')[0]
    tmp_dir = os.path.join('/tmp', str(id_))
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    tmp_file = tmp_dir + '.zip'

    with open(tmp_file, 'wb') as f:
        for chunk in session.get(
            url, headers=headers
        ).iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    with ZipFile(tmp_file) as tar:
        for name in [i for i in tar.namelist() if i != 'index']:
            tar.extract(name, path=tmp_dir)
    # os.remove(tmp_file)
    return tmp_dir


def save_ugoku(url):
    html = get_html(url)
    ugoku_json = parse_html(html)
    ugoku_zip = ugoku_json['src']
    dirname = download_zip(ugoku_zip)
    fps = 1000 / 80
    subprocess.check_call(
        'ffmpeg -i "{dirname}/%6d.jpg" -y {output}'.format(
            fps=fps, dirname=dirname, output='pixiv.mp4'
        ),
        shell=True
    )


def cli():
    import fire
    fire.Fire(save_ugoku)
