from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="screeve-embeddings",
    version="0.1.0",
    author="Nargizi",
    author_email="supasuperdin@gmail.com",
    description="pre-trained word2vec embeddings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)