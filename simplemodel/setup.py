from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="simplemodel",
    version="0.1.0",
    url="https://github.com/axsaucedo/simplemodel.git",
    author="axsaucedo",
    author_email="",
    description="A short description of the project.",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "mlserver==1.1.0",
    ],
    long_description=Path("README.md").read_text(),
    license="MIT",
)

