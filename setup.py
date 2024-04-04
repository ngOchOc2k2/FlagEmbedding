from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='FlagEmbedding',
    version='1.2.8',
    description='FlagEmbedding',
    long_description=readme,
    url='https://github.com/ngOchOc2k2/FlagEmbedding',
    packages=find_packages(),
    install_requires=[
        'torch>=1.6.0',
        'transformers>=4.33.0',
        'datasets',
        'accelerate>=0.20.1',
        'sentence_transformers',
    ],
)