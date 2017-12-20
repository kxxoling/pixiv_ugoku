#!/usr/bin/env python
from setuptools import setup

setup(
    name='pixiv_ugoku',
    version='0.1.1',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ugoku = pixiv_ugoku:cli',
        ]
    },
    install_requires=[
        'requests >= 2.5.0, != 2.15, != 2.16',
        'fire>=0.1.2',
        'six>=1.8',
    ],
    classifiers=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ],
    license='MIT',
    description='Simple Pixiv animated image downloader.',
    author='Kane Blueriver',
    author_email='kxxoling@gmail.com',
    url='https://github.com/kxxoling/pixiv_ugoku'
)
