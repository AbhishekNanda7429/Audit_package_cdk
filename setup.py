from setuptools import setup, find_packages

setup(
    name='my_package',
    version='2.0.0',
    description='Package for taking JSON input and uploading to S3',
    packages=find_packages(),
    install_requires=['boto3'],
)