from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_sc",
    version="0.0.2",
    author="SauloCarvalho",
    description="Image Processing Program",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saulocarvalho/Image-Processing-Package-SC.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.',
)