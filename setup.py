from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    requirement_items = open('requirements.txt', 'r')
    for item in requirement_items:
        requirement_list.append(item) 
    
    return requirement_list

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """

setup(
    name="sensor",
    version="0.0.1",
    author="Vineet Bhardwaj",
    author_email="vineet.100@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)

