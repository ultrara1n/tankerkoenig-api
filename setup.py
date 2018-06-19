import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytankerkoenig",
    version="0.0.5",
    author="Philipp Wensauer",
    author_email="mail@philippwensauer.com",
    description="Library for Tankerkoenig.de JSON API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ultrara1n/tankerkoenig-api",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ),
)
