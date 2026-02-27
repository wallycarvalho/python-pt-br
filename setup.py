#!/usr/bin/env python
"""Setup configuration for python-pt-br package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-pt-br",
    version="0.1.0",
    author="OpenCode",
    author_email="opencode@example.com",
    description="Write Python code in Portuguese Brazilian",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/python-pt-br",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Natural Language :: Portuguese (Brazilian)",
    ],
    python_requires=">=3.8",
    install_requires=[],  # No external dependencies for MVP
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
        ],
    },
    entry_points={},
)
