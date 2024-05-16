from __future__ import division

from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()


def parse_requirements_file(path):
    with open(path) as fp:
        dependencies = (d.strip() for d in fp.read().split("\n") if d.strip())
        return [d for d in dependencies if not d.startswith("#")]


setup(
    name="mailtm-sdk",
    version="0.1.0",
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
    requires=parse_requirements_file("requirements.txt"),
)
