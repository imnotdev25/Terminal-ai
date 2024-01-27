from setuptools import find_packages
from setuptools import setup

setup(
    name="terminalai",
    version="0.0.5",
    license="GNU General Public License v2.0",
    author="Talaviya Bhavik",
    author_email="talaviyabhavik@proton.me",
    description="AI Terminal assistant",
    packages=find_packages("terminalai"),
    package_dir={"": "terminalai"},
    url="https://github.com/imnotdev25/Terminal-ai",
    project_urls={
        "Bug Report": "https://github.com/imnotdev25/Terminal-ai/issues/new",
    },
    install_requires=[
        "google-generativeai",
        "httpx",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["term-ai"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
