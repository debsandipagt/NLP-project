"""
# This will automatically include all packages (directories containing an __init__.py file) in the source directory. 
# It ensures that all relevant Python modules are included when the package is built.
"""
import sys
import os
from src.constant import HYPEN_E_DOT
from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath:str) -> List[str]:
    """
    This function will return list of requirements
    """
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='nlp-text-classification-project',
    version='0.0.1',
    author='Sandip Deb',
    auther_email='debsandip.agt@gmail.com',
    packages=find_packages(), 
    install_requires = get_requirements('requirements.txt'),
    )