# Copyright (c) 2022 aerocyber
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meteorpy",
    version="0.0.4-dev0",
    author="aerocyber",
    description="A tool to share python environment by building it from scratch on target machines.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aerocyber/meteorpy/",
    project_urls={
        "Bug Tracker": "https://github.com/aerocyber/meteorpy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "meteorpy"},
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'yourscript = meteorpy.__main__:env',
        ],
    },
)
