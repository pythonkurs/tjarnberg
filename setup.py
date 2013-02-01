from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tjarnberg',
    version=version,
    description="Learning python",
    long_description="""Even more learning python""",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='python science',
    author='Andreas Tj\xc3\xa4rnberg',
    author_email='andreas.tjarnberg@scilifelab.se',
    url='scilifelab.se',
    license='GPLv3',
    scripts = ['scripts/getting_data.py', 'scripts/check_repo.py'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['untangle', 'requests'],
    entry_points="""# -*- Entry points: -*-""",
    )
