from setuptools import setup, find_packages
from io import open
import re


def read(filename):
	with open(filename, "r", encoding="utf-8") as file:
		return file.read()


with open("vktools/version.py", "r") as file:
	version = re.findall(r"[0-9]+.[0-9]+.[0-9]+", file.read())[0]

setup(name="vktools",
	version=version,
	description="Инструменты для модуля vk-api. Клавиатура и карусели.",
	long_description=read("README.md"),
	long_description_content_type="text/markdown",
	url="https://github.com/Fsoky/vktools",
	author="Fsoky Community",
	author_email="cyberuest0x12@gmail.com",
	keywords="vktools vk vk-api api",
	packages=find_packages()
)