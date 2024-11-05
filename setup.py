from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name="math_quiz", 
    version="1.1.0",  
    author="Punith sai reddy",
    description="A simple math quiz package",
    long_description=open("README.md").read(),
    url="https://github.com/punithsaireddy/DSSSHW2.git", 
    packages=find_packages(), 
    python_requires=">=3.6",
    install_requires=parse_requirements('requirements.txt')
)
