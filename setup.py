import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-templatetag-handlebars',
    version='1.3.2.dev0',
    author='Mathieu Leplatre',
    author_email='mathieu.leplatre@makina-corpus.com',
    url='https://github.com/HiveHQ/django-templatetag-handlebars',
    description="Easily embed Handlebars.js templates in your django templates",
    license='LPGL, see LICENSE file.',
    install_requires=['django'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=['Topic :: Utilities',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Development Status :: 5 - Production/Stable',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3'],
)
