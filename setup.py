import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datahen",
    version="0.3.1",
    author="Datahen",
    author_email="services@datahen.com",
    description="Datahen package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://datahen.com",
    packages=setuptools.find_packages(),
    entry_points ={ 
        'console_scripts': [ 
            'datahen = datahen.CLI:main'
        ] 
    }, 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
      'requests'
    ],
    python_requires='>=3.6',
)