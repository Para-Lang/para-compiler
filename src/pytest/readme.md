# Para-C Compiler Tests

## Quick Setup for Testing

### Installation of pytest

```bash
python3 -m pip install pytest 
```

Installing inside the main dir of the project the current state of the module so it can be used for testing:
```bash
python3 -m pip install -e .
```

## Running with Coverage

### Install `coverage.py` for coverage testing

```bash
python3 -m pip install coverage
```

### Coverage Testing

Using coverage the standard unit-testing will be modified and watched to see what code-paths are not tested 
and might need to be included as well. It will return a regular report but create a new `.coverage` file

```bash
coverage run -m pytest
```

### Creating a coverage badge

Creating a coverage badge for the testing can be easily done using:

```bash
coverage-badge -o coverage.svg
```

### Viewing the Report in HTML

Inside the test directory:

```bash
coverage html
```
