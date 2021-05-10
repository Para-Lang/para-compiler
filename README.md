![para-c](https://socialify.git.ci/Luna-Klatzer/para-c/image?description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FLuna-Klatzer%2FPara-C%2Fmain%2FPara-C.png&owner=1&pattern=Charlie%20Brown&pulls=1&stargazers=1&theme=Light)

<br>
<br>
<br>

*Para-C is not intended to be a widely „optimised“ or „production-ready“ programming language. It is solely a free-time
project designed for learning and testing purposes, which we do not intend for anything other than that.*

## Summary

Para-C (gre. beside C) is a new programming language designed to integrate C and serve as a helper and simplifier to write better C code. 
To achieve that, it will introduce more features, such as  new built-in Macros and functions, OOP structures, 
more straightforward array and malloc-handling, expanded data types and simplified functions. 

Still, unlike others to make an entirely new language with new syntax, systems and logic, Para-C is built to have a simpler syntax and structure similar to Python and TypeScript, but with direct compatibility with C using its speed in the compiled execution. (Comparable to JS and TS)

It will serve as a helper and extension to C and provide features and more manageable implementations to achieve more in less time. So, programming in Para-C will be similar, but still in its way simpler and well looking.

## Development

![Deploy and test workflow](https://github.com/Luna-Klatzer/Para-C/actions/workflows/python-test.yml/badge.svg)

### Building

The building process is relatively simple but requires multiple steps and 

#### Build for specified OS

This specified script will automatically build the project and create a folder containing all the required data as
well as the .exe file, which will be the compiler itself

```bash
python ./src/build-exe.py
```

After that, the installer can be created with the passed .exe for the compiler

#### Build inno-setup installer for Windows 

Download inno-setup [here](https://jrsoftware.org/download.php/is.exe)

Build inside this folder and use the inno-setup.iss file. The generated installer will be placed inside /Output

### Installation
 
To install Para-C, you can either use the pre-built installer for the specified version or build the compiler yourself and run
the installer afterwards. (Only building the compiler will not be enough, since the configuration of the installer needs
to be run so that the )
