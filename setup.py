from setuptools import setup, find_packages

setup(
    name="DataCleanPro",  
    version="0.1.0",  
    author=".",
    author_email=".",
    description="A data preprocessing and visualization toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/selmayilmaz13/DataCleanPro",  
    packages=find_packages(),  
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn"
    ],
   
    python_requires=">=3.6",
)
