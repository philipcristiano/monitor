#!/usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='monitor',
    version='0.0.1',
    description='A daemon to monitor system behavior',
    keywords = 'testing',
    url='https://github.com/philipcristiano/monitor',
    author='Philip Cristiano',
    author_email='monitor@philipcristiano.com',
    license='BSD',
    packages=['monitor', 'monitor.monitors'],
    namespace_packages=['monitor.monitors'],
    install_requires=[
        'importlib',
        'puka',
    ],
    test_suite='tests',
    long_description=read('README.md'),
    zip_safe=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    entry_points="""
    [console_scripts]
    monitor = monitor.daemon:main
    """,
)
