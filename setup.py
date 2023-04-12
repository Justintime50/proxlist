import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'beautifulsoup4 == 4.*',
    'requests == 2.*',
    'woodchips == 0.2.*',
]

DEV_REQUIREMENTS = [
    'bandit == 1.7.*',
    'black == 23.*',
    'build == 0.10.*',
    'flake8 == 5.*',
    'isort == 5.*',
    'mypy == 1.2.*',
    'pytest == 7.*',
    'pytest-cov == 4.*',
    'twine == 4.*',
    'types-requests',
]

setuptools.setup(
    name='proxlist',
    version='0.5.1',
    description='Retrieve proxy servers.',
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
    python_requires='>=3.7, <4',
)
