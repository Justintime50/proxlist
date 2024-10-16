import re

import setuptools


with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

# Inspiration: https://stackoverflow.com/a/7071358/6064135
with open('proxlist/_version.py', 'r') as version_file:
    version_groups = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_groups:
        version = version_groups.group(1)
    else:
        raise RuntimeError('Unable to find version string!')

REQUIREMENTS = [
    'beautifulsoup4 == 4.*',
    'requests == 2.*',
    'woodchips == 1.*',
]

DEV_REQUIREMENTS = [
    'bandit == 1.7.*',
    'black == 24.*',
    'build == 1.1.*',
    'flake8 == 7.*',
    'isort == 5.*',
    'mypy == 1.11.*',
    'pytest == 8.*',
    'pytest-cov == 4.*',
]

setuptools.setup(
    name='proxlist',
    version=version,
    description='Retrieve free, open-source proxy servers.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/Justintime50/proxlist',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(
        exclude=[
            'examples',
            'test',
        ]
    ),
    package_data={
        'proxlist': [
            'py.typed',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    python_requires='>=3.8, <4',
)
