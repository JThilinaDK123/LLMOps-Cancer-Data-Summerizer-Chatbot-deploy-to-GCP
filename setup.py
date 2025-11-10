from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Cancer-data-pdf-Summerizer-Chatbot",
    version="0.1",
    author="Thilina",
    packages=find_packages(),
    install_requires = requirements,
)