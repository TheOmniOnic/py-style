from setuptools import setup, find_packages

setup(
    name="py-style",  
    version="0.0.1",  
    description="A terminal text formatting package with 24-bit color support",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="TheOmniOnic",  
    packages=find_packages(where="."),
    package_dir={"": "."},
    include_package_data=True,
    install_requires=[],
    url="https://github.com/TheOmniOnic/py-style",
    python_requires=">=3.6",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Terminals",
    ],
)
