from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        # filter out comments and empty lines
        lines = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
    return lines

# Read requirements from requirements.txt
requirements = parse_requirements('requirements.txt')

setup(
    name='inventory_management',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'inventory_management_run = app.py'
        ]
    },
    author='Rahul Sharma',
    author_email='reethified@email.com',
    description='An Inventory Management web application built with GPT prmompts',
    long_description=open('README.md').read(),
    license='TODO',
    classifiers=[
        'Programming Language :: Python :: 3'
        'Operating System :: OS Independent'
    ],
)
