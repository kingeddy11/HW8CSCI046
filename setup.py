import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_Wu_containers",
    version="1.0.0",
    description="Created a Containers project for CMC's CSCI046: Data Structures and Algorithms class with Professor Izbicki. Package includes Binary Trees, Binary Search Trees, AVL Trees, and Heap Trees.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kingeddy11/HW8CSCI046",
    author="Edward Wu",
    author_email="ewu23@cmc.edu",
    license="BSD-3-Clause",
    classifiers=[
        "License :: OSI Approved :: BSD-3-Clause License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)
