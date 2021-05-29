#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='django-carousels',
    version='0.1.3',
    description='Django app for model-based carousels',
    long_description=open('README.md').read(),
    author='Pragmatic Mates',
    author_email='info@pragmaticmates.com',
    maintainer='Pragmatic Mates',
    maintainer_email='info@pragmaticmates.com',
    url='https://github.com/PragmaticMates/django-carousels',
    packages=find_packages(),
    include_package_data=True,
    install_requires=('django',),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Development Status :: 3 - Alpha'
    ],
    license='GNU General Public License (GPL)',
    keywords="django UI carousel",
)
