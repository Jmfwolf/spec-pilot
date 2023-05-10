from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="spec-pilot",
    version="0.3.2",
    description="A command-line tool for generating and managing OpenAPI specifications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="jmfwolf",
    author_email="jmfwolf@hacksomniac.com",
    url="https://github.com/jmfwolf/spec-pilot",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "spec-pilot=spec_pilot.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.6',
)