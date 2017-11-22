#!/usr/bin/env python
from setuptools import setup

setup(
    name='pixiv_ugoku',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ugoku = pixiv_ugoku:cli',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ],
    license="MIT",
    description='',
    author='Kane Blueriver',
    author_email='kxxoling@gmail.com',
    url='https://github.com/kxxoling/pixiv_ugoku'
)
