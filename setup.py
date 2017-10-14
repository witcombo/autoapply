import os
import setuptools

root = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name = 'autoapply',
    version = '0.1.0',
    description = 'Automatically apply changes from a remote URL to the Kubernetes cluster',
    long_description = long_description,
    url = 'https://github.com/pascalgn/autoapply',
    author = 'Pascal',
    license = 'ISC',
    packages = setuptools.find_packages(include=['autoapply']),
    scripts = ['bin/autoapply']
)