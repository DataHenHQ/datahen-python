import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datahen",
    version="0.4",
    author="Datahen",
    author_email="services@datahen.com",
    description="Datahen package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://datahen.com",
    packages=setuptools.find_packages(),
    entry_points ={ 
        'console_scripts': [ 
            'hen-python = datahen.CLI:main'
        ] 
    }, 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
      'beautifulsoup4',
      'requests'
    ],
    python_requires='>=3.6',
)