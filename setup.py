import os
from imp import load_source
from setuptools import setup, find_packages
from glob import glob

__version__ = load_source('pystac.version', 'pystac/version.py').__version__

from os.path import (
    basename,
    splitext
)

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    install_requires = f.read().split('\n')

with open(os.path.join(here, 'README.md')) as readme_file:
    readme = readme_file.read()

setup(
    name='pystac',
    version=__version__,
    description=("Python library for working with Spatiotemporal Asset Catalog (STAC)."),
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Azavea",
    author_email='info@azavea.com',
    url='https://github.com/azavea/pystac.git',
    packages=find_packages(),
    py_modules=[splitext(basename(path))[0] for path in glob('pystac/*.py')],
    include_package_data=False,
    install_requires=install_requires,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=[
        'pystac',
        'imagery',
        'raster',
        'catalog',
        'STAC'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests'
)
