# -*- coding: utf-8 -*-
from setuptools import setup

__author__ = 'viruzzz-kun'
__version__ = '0.1'


if __name__ == '__main__':
    setup(
        name="bouser_db",
        version=__version__,
        description="Database service for Bouser",
        long_description='',
        author=__author__,
        author_email="viruzzz.soft@gmail.com",
        license='ISC',
        url="http://github.com/hitsl/bouser_db",
        packages=[
            "bouser_db",
        ],
        zip_safe=False,
        package_data={},
        install_requires=[
            'bouser',
            'sqlalchemy',
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Plugins",
            "Programming Language :: Python",
        ])
