import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

install_requires = [
    'ipython>=1.0',
    'shortuuid'
]

setup(
    name='postgresql_syntax_checker_magic',
    py_modules=['postgresql_syntax_checker_magic'],
    version='0.1',
    description='Check syntax of postgresql via ipython',
    long_description=README,
    author='Eyal Trabelsi',
    author_email='eyaltrabelsi@gmail.com',
    url='https://github.com/eyaltrabelsi/postgresql_syntax_checker_magic',
    keywords=['sql', 'ipython', 'syntax'],
    install_requires=install_requires
)
