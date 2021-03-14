from setuptools import setup, find_packages

des: str = """
Implementation of all data structures that I am interested in.

DON'T INSTALL IT EXPECTING A SERIOUS PACKAGE. It´s just a ton of
practice code that will make me proud someday.
"""

setup(
    name="Structures",
    version="1.0",
    author="Alex050218",
    url="https://github.com/Alex050218/Custom_structures",
    author_email="alejandrovalenzuela051@gmail.com",
    description=des,
    packages=find_packages(exclude=("tests",))
)
