from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name="aaispy",
    version="0.0.1",
    description="Python wrapper around the Andrews & Arnold API",
    long_description=readme(),
    keywords=["aaisp", "isp", "api"],
    url="https://github.com/rjevski/aaispy",
    author="Andre Borie",
    author_email="hello@andreborie.name",
    license="MIT",
    packages=["aaispy"],
    install_requires=["requests"],
    include_package_data=True)