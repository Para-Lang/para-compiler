![para-c](https://socialify.git.ci/Luna-Klatzer/para-c/image?description=1&font=Source%20Code%20Pro&forks=1&issues=1&language=1&owner=1&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Light)

<br>
<br>
<br>

*Para-C is not intended to be a widely „optimised“ or „production-ready“ programming language. It is solely a free-time
project designed for learning and testing purposes, which we do not intend for anything other than that.*

## Summary

Para-C is a new programming language designed to integrate C and serve as a helper and simplifier to write better C code. 
Including adding more features, like new built-in Macros and functions, OOP-structures, 
more straightforward array and malloc-handling, expanded data types and simplified functions. 

Still, unlike others to make an entirely new language with new syntax, systems and logic, it is built around to have
just a simpler syntax and structure similar to Python and TypeScript but can include directly code from C and use its 
speed in the compiled execution. 

It will serve as a helper but also extension to C and provide features and easier implementations to achieve more in 
less time. So, programming in Para-C will be similar, but still in its way simpler and well looking. Syntax-wise it 
will still lay onto C to avoid causing issues and additional compiler-code. Despite the partly different look and 
functions, the writing style will have a similar feel to C.

## Development

### Building

The building process is relatively simple, but requires multiple steps and 

#### Build for specified OS

This specified script will automatically build the project and create a folder containing all the required data as
well as the .exe file which will be the compiler itself

```bash
python ./src/build-exe.py
```

After that the installer can be created with the passed .exe for the compiler

#### Build inno-setup installer for Windows 

Download inno-setup [here](https://jrsoftware.org/download.php/is.exe)

Build inside this folder and use the inno-setup.iss file. The generated installer will be placed inside /Output

### Installation
 
To install Para-C either use the pre-built installer for the specified version or build the compiler yourself and run
the installer afterwards. (Only building the compiler will not be enough, since the configuration of the installer needs
to be run so that the )