from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirement(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = 'MLProject',
    author = 'Saurabh',
    author_email='vishwakarma.20august@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    requires=get_requirement('requirements.txt')
)