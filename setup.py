from setuptools import setup, find_packages

VERSION='0.0.1'

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='browse_for_what',
    version=VERSION,
    description='Let your computer randomly browse the internet via random Google searches',
    long_description=readme,
    author='Bill Riehl',
    author_email='briehl@gmail.com',
    url='https://github.com/briehl/browse-for-what',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
