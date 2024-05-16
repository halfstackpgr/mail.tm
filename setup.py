from __future__ import division

from setuptools import setup

with open('README.md', "r", encoding="utf-8") as f:
    description = f.read()

setup(
    name="mailtm-sdk",
    version="0.1.0",
    description="Mail.tm Stack Development Kit, designed to enhance your experience with the renowned temporary email service, mail.tm",
    long_description=description,
    long_description_content_type="text/markdown"
    author="Parth Mishra",
    author_email="halfstackpgr@gmail.com", 
    maintainer="Parth Mishra", 
    maintainer_email="halfstackpgr@gmail.com",
    url="https://halfstackpgr.github.io/Mail.tm/",
    packages=["mailtm", "mailtm.abc", "mailtm.core", "mailtm.impls", "mailtm.server"],
    entry_points={"console_scripts": ["mailtm=mailtm"]}
)