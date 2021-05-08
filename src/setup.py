import setuptools

with open("../README.md", "r") as file:
    long_description = file.read()

with open("requirements.txt") as file:
    requirements = file.read()

setuptools.setup(
    name="parac_compiler",
    version="0.1",
    author="Luna Klatzer",
    author_email="luna.klatzer@gmail.com",
    description="Python-Compiler for Para-C",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU GENERAL PUBLIC LICENSE v3.0",
    url="https://github.com/Luna-Klatzer/Para-C/",
    project_urls={
        "Issue-Page": "https://github.com/Luna-Klatzer/Para-C/issues/",
        "Changelog": "https://github.com/Luna-Klatzer/Para-C/releases"
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=requirements
)
