import os
from setuptools import find_packages, setup

__version__ = '0.8'

# We use the README as the long_description
readme_path = os.path.join(os.path.dirname(__file__), "README.rst")


setup(
    name='asgi_redis',
    version=__version__,
    url='http://github.com/andrewgodwin/asgi_redis/',
    author='Andrew Godwin',
    author_email='andrew@aeracode.org',
    description='Redis-backed ASGI channel layer implementation',
    long_description=open(readme_path).read(),
    license='BSD',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'six',
        'redis>=2.10',
        'msgpack-python',
    ]
)
