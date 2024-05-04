# if i want to install local package in virtual env for that we use this setup.py file /or/  then we need a setup.py file
from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Nitish kumar',
    author_email=' nce2226@gmail.com',
    install_requires=["huggingface","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)