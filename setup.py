from setuptools import setup, find_packages

setup(
    name='inventory_management',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'streamlit-auth',
        'pyyaml',
        'unittest2'
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'inventory_management_run = frontend.streamlit_app:main'
        ]
    },
    author='Rahul Sharma',
    author_email='reethified@email.com',
    description='An Inventory Management web application built with Streamlit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/inventory_management',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
