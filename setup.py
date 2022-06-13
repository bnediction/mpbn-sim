#!/usr/bin/env python

from setuptools import setup

NAME = "mpbn_sim"
VERSION = "0.1"

setup(name=NAME,
    version=VERSION,
    author="Loïc Paulevé",
    author_email="loic.pauleve@labri.fr",
    url="https://github.com/bnediction/mpbn-sim",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords='',
    description="Simulation of Most Permissive Boolean networks",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "mpbn",
        "numpy",
        "scipy",
        "tqdm",
    ],
    entry_points={
        "console_scripts": [
            "mpbn_sim=mpbn_sim:cli",
        ],
    },
    packages=[NAME],
)
