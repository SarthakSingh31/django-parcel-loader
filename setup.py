from setuptools import setup

VERSION = '0.0.1'

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='django-parcel-loader',
    version=VERSION,
    author='Sarthak Singh',
    author_email='ss269@uw.edu',
    description='A minimal config bundle loader for parcel',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SarthakSingh31/django-parcel-loader',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
)
