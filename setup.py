import pathlib

from setuptools import setup

# BASE PATH
BASE = pathlib.Path(__file__).parent

# README TEXT
README = (BASE / "README.md").read_text()

# Setup
setup(
    name="dspython",
    version="0.0.1",
    description="",
    author="its-kumar",
    license="MIT",
)
