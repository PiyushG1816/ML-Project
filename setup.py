from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) -> list[str]:    # This will return the list of requirements

    requirements = []

    with open(file_path) as required:
        requirements= required.readlines()
        requirements = [i.replace('\n',"") for i in requirements]

    return requirements



setup(
    name='ML Project',
    version='0.0.1',
    author='Piyush',
    author_email='pg.piyushgpt18@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)