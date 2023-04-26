import os
from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        self.execute(lambda: self.download_spacy_model(), [])

    @staticmethod
    def download_spacy_model():
        os.system("python -m spacy download en_core_web_sm")

setup(
    name="spec_pilot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here
        "spacy",
        "pystache",
        "PyYaml"
    ],
    entry_points={
        "console_scripts": [
            "spec_pilot=spec_pilot:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    cmdclass={"install": PostInstallCommand},
)
