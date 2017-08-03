import re
import codecs
import os
from setuptools import setup, find_packages


def read(*parts):
    path = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(path, encoding='utf-8') as fobj:
        return fobj.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def dependencies():
    deps = []
    for line in open('requirements.txt').readlines():
        deps.append(line.strip('\n'))
    return deps


setup(
    name="JiraCLI",
    version=find_version("jiracli", "__init__.py"),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jira=jiracli:main',
        ],
    },
    install_requires=dependencies()
)