# -*- coding: utf8 -*-
"""
setup du module bdd_comptage
lancement auto avec "if name=main app.run()"
"""

from setuptools import setup
from battuesha.app import APP

setup(
    name='BDD_BattuesHA',
    version='0.1.3',
    url='https://pypi.org/',
    description='- desc -',
    long_description='README',
    long_description_content_type='text/markdown',
    author='Pierre M',
    author_email='pierremanchon8@gmail.com',
    license='GNU GPL 3.0',
    packages=['battuesha'],
    include_package_data=True,
    install_requires='requirements',
)
if __name__ == '__main__':
    APP.run()
