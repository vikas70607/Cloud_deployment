from setuptools import find_packages,setup
from typing import List

hypen = '-e .'

def get_requirements(file_path:str) -> List[str]:
    # return list of requirements
    requirements = []
    with open(file_path, 'r') as file_path:
        requirements = file_path.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if hypen in requirements:
            requirements.remove(hypen)
            
    return requirements

setup(
name='cloud',
version='0.0.1',
author='Vikas',
author_email='vikas70607@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)