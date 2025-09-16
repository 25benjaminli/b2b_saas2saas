from setuptools import setup, find_packages

setup(
    name="b2bsaas2saas",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "openai"
    ],
    entry_points={
        "console_scripts": [
            "b2bsaas2saas=b2bsaas2saas.main:get_random_saas_idea"
        ]
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A package to generate random SaaS ideas using ChatGPT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/b2bsaas2saas",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)