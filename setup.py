# coding=utf-8

from setuptools import setup
from wannaquark.utils.constants import Constants as Cte

#  long_description=open('README.md').read(),
#  https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/

setup(
    name=Cte.PACKAGE_NAME,
    version=Cte.VERSION,
    author=Cte.AUTHOR,
    author_email=Cte.EMAIL,
    packages=[Cte.PACKAGE_NAME],
    scripts=[],
    url=Cte.URL_PROJECT,
    license='LICENSE',
    description=Cte.DESCRIPTION,
    install_requires=open('requirements.txt').read().split("\n"),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
















