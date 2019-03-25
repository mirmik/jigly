#!/usr/bin/env python3

from setuptools import setup
import glob
import os

setup(
	name = 'jigly',
	packages = ['jigly'],
	version = "0.0.1",
	license='MIT',
	description = 'UDP datagramm based audio protocol/server.',
	author = 'Sorokin Nikolay',
	author_email = 'mirmikns@yandex.ru',
	url = 'https://github.com/mirmik/jigly',
	long_description=open("README.md", "r").read(),
	long_description_content_type='text/markdown',
	keywords = ['music', 'udp'],
	classifiers = [],

	#scripts = ["configurator/licant-libs"],
)
