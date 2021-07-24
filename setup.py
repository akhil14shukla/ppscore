from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    
    
setup(
    name='PyCustom',
    packages=find_packages(),
    version='0.1.0',
    description='Customised Python Functions',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/akhil14shukla/PyCustom",
    author='Akhil Shukla (akhil14shukla)',
    license='GNU v3.0',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)