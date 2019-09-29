import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fantasy-database-2019-thecasper2",
    version="0.0.1",
    author="Alex Dolphin",
    author_email="alex.dolphin@dolphindata.co.uk",
    description="Writes Fantasy Football API data to a database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thecasper2/fantasy-database-2019",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    tests_require='pytest'
)