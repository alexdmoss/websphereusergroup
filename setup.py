from setuptools import setup, find_packages

setup(
    name="wug",
    packages=find_packages(where='.'),
    include_package_data=True,
    package_dir={'': '.'}
)
