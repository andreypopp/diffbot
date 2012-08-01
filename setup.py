from setuptools import setup, find_packages
import sys, os

version = '0.2'
install_requires = [
    'urllib3',
    'simplejson',
    ]

setup(
    name='diffbot',
    version=version,
    description='diffbot api',
    author='Andrey Popp',
    author_email='8mayday@gmail.com',
    url="https://github.com/andreypopp/diffbot",
    py_modules=['diffbot'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    )
