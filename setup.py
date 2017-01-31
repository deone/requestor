# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='requestor',
    version='0.1.1',
    description='Use this package to make HTTP post calls to django APIs with csrf support, and return response in json.',
    long_description=long_description,
    url='https://github.com/deone/requestor',
    author='Dayo Osikoya',
    author_email='alwaysdeone@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='http post requests json response django csrf',
    py_modules=["requestor"],
    install_requires=['requests'],
)
