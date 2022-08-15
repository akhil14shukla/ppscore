from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas>=1.0.0,<2.0.0", "scikit-learn >= 0.20.2, < 1.0.0"]

setup(
    name='ppscore',
    packages=find_packages(),
    version='0.0.4',
    description='Customised Python Functions for calculating Predictive Power Score',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/akhil14shukla/ppscore",
    author='Akhil Shukla (akhil14shukla)',
    license='GNU v3.0',
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
