"""Setup for videojsXBlock."""

import os

from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='videojs-xblock',
    version='1.0.5',
    description='XBlock to use the Video.js player in edX, instead of the default one.',
    packages=[
        'videojs',
    ],
    install_requires=[
        'XBlock',
        'pycaption==0.7.3',
        'cssutils==0.9.10'
    ],
    entry_points={
        'xblock.v1': [
            'videojs = videojs:videojsXBlock',
        ]
    },
    package_data=package_data("videojs", "static"),
)
