import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'beautifulsoup4 == 4.*',
    'requests == 2.*',
    'woodchips == 0.2.*',
]

DEV_REQUIREMENTS = [
    'black',
    'coveralls == 3.*',
    'flake8',
    'isort',
    'mypy',
    'pytest == 7.*',
    'pytest-cov == 3.*',
    'types-requests',
]

setuptools.setup(
    name='proxlist',
    version='0.4.0',
    description='Retrieve proxy servers.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/Justintime50/proxlist',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    package_data={'proxlist': ['py.typed']},
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
