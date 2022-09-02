import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="sys-monit-technoabsurdist",
    version="0.0.1",
    author="Emi Andere",
    author_email="andere@uchicago.edu",
    description="A simple system monitoring python tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/technoabsurdist/sysMonit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
