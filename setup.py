# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in short_courses/__init__.py
from short_courses import __version__ as version

setup(
	name="short_courses",
	version=version,
	description="It is a short courses app",
	author="Shakila Sahira",
	author_email="nurshakila2000@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
