from setuptools import setup, find_packages

setup(
    name="weathergovapi",
    version="1",
    packages=find_packages(exclude=["Examples*"]),
    license="MIT",
    description="Weather Functions and Data From NWS",
    long_description=open("README.md").read(),
    install_requires=["requests","json"],
    url="https://github.com/MatthewIsHere/Weather.Gov-APi",
    author="Matthew Lyon",
    author_email="matthew@matthewlyon.net"
)
