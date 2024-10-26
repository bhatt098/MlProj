from setuptools import find_packages,setup
from typing import List

hypen="-e ."
#Meta data infomation about proj

def get_requirements1(fileName:str)->List[str]:
    with open(fileName) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in f if requirements]

        if hypen in requirements:
            requirements.remove(hypen)
    return requirements


def get_requirements(fileName:str)->List[str]:
    with open(fileName) as f:
        requirements=[req.strip() for req in f if req.strip() and req.strip()!='-e .']
    return requirements

setup(   
name='MLProj',
version='0.0.1',
author='Mohit',
author_email='bhattmohit728@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)


        # requirements=f.readlines();
        #strip() string method used to remove whitespaces,'\n' and all
        # if()



