from setuptools import setup, find_packages

setup(
    name="b2b_saas2saas",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv"
    ],
    author="Benjamin Li",
    author_email="25benjaminli@gmail.com",
    description="A package to generate random SaaS ideas using ChatGPT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/25benjaminli/b2b_saas2saas",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)