import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytankerkoenig",
    version="0.0.6",
    author="Philipp Wensauer",
    author_email="mail@philippwensauer.com",
    description="Library for Tankerkoenig.de JSON API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ultrara1n/tankerkoenig-api",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ),
)
