from __future__ import annotations
from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()


setup(
    name="mailtm-sdk",
    version="0.1.3",
    description="Mail.tm Stack Development Kit, designed to enhance your experience with the renowned temporary email service, mail.tm",
    long_description=description,
    long_description_content_type="text/markdown",
    author="Parth Mishra",
    author_email="halfstackpgr@gmail.com",
    maintainer="Parth Mishra",
    maintainer_email="halfstackpgr@gmail.com",
    url="https://halfstackpgr.github.io/Mail.tm/",
    packages=find_namespace_packages(include=["mailtm*"]),
    entry_points={"console_scripts": ["mailtm = mailtm.cli:version"]},
    install_requires=["aiohttp", "requests", "msgspec", "colorama"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
)
