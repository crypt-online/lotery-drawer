import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lotery-drawer",
    version="1.0.1",
    author="Crypt Online",
    author_email="admin@hxrobot.io",
    description="A simple, proven and non-falsifiable lottery draw tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crypt-online/lotery-drawer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)