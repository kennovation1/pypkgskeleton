# Purpose
This project provides a starting point skeleton for an internal
Python package that can be distributed by providing Git pointers
or tarballs. That is, there is no need to publish the package to a PyPi
server to distribute to internal teams and collaborators.

The intended audience is Python developers that don't have much
packaging experience and just want to get something working.
The motivation was that there are a million different ways to package
Python and an equal number of tutorials and blogs posts. I found it to be
a deep yak shearing experience that never seemed to converge.
Likely the fault is mine by being inexperienced with packaging, but I imagine
I'm not the only one. Therefore, this annotated example will strive to make
something usable for a couple of very common cases. This example does not
intend to cover complex or more varied use cases. Being clear for a limited
purpose is chosen over being confusing but covering many use cases.

To be clear, this is not being written by an expert. This works, but people
that know what they are actually doing might find lots of ways to improve
this. Contributions are most welcome (please just keep the focus on clarity for
the select limited use cases).

Ultimately the following is very simple. It's interesting that it took
a lot of effort to remove all of the extra noise any variability that exists
in standard documentation to distill down the the practical essentials.

## References
There are many internet resources for Python packaging. Unfortunately they all seem
fairly divergent. One resource that I found to be particuilarly useful
in developing this project was: https://changhsinlee.com/python-package/

# Setup
You should do all of the following in a Python virtual environment.
Describing virtual environments is beyond the scope of this project.
I'll assume you are using Python 3.7 or greater.

## One virtual environment example
I don't want to digress by talking about virtual environments, but as a quick
example, here's what I use (assumes pyenv, virtualenv, and virtualenvwrapper are installed).
```
pyenv local 3.8.10  # One-time. Creates a .python-version file
mkvirtualenv skeleton -p `pyenv which python`  # Creates virtual environment and activates it
workon skeleton  # Use this to activate `skeleton` when creating a new shell
```

## One time installation of build tools
```
pip install -q build
```

# Directory structure
Below is our example directory structure showing files we created
and files that are created by the build.
This example shows top-level modules in the package root and two sub-packages,
each with multiple modules.

You can delete one or both subpackages or add more.
You can have one or more modules in the root package.

*NOTE:* Do not name a top module to be the same as the package name.
For example having a top module called pypkgskeleton.py in the
pypkgskeleton package will cause an import error.
Another error to avoid is don't make the only difference
be just case differences since that is not a sufficient distinction.

Below, we'll look at configuring `__init__.py` to show different ways
of allowing the client program to more easily import modules.

```
pypkgskeleton/
????????? README.md                  # Provide this markdown file
????????? build/                     # Created by build
??????? ????????? bdist.macosx-11.4-arm64
??????? ????????? lib/
???????     ????????? pypkgskeleton/
???????         ????????? __init__.py
???????         ????????? subpkg1/
???????         ??????? ????????? __init__.py
???????         ??????? ????????? module1.py
???????         ??????? ????????? module2.py
???????         ????????? subpkg2/
???????         ??????? ????????? __init__.py
???????         ??????? ????????? module1.py
???????         ??????? ????????? module2.py
???????         ????????? topmodule1.py
???????         ????????? topmodule2.py
????????? dist/                      # Created by build. Use these files to install
??????? ????????? pypkgskeleton-0.1.0-py3-none-any.whl
??????? ????????? pypkgskeleton-0.1.0.tar.gz
??????? ????????? pypkgskeleton-0.1.1-py3-none-any.whl
??????? ????????? pypkgskeleton-0.1.1.tar.gz
????????? pypkgskeleton/             # Create this to match package name. import pypkgskeleton
??????? ????????? __init__.py            # May be empty or have some imports. Indicates pypkgskeleton is a package
??????? ????????? subpkg1/               # import pypkgskeleton.subpkg1
??????? ??????? ????????? __init__.py        # Usually empty. Indicates that subpkg1 is a sub-package
??????? ??????? ????????? module1.py
??????? ??????? ????????? module2.py
??????? ????????? subpkg2/               # import pypkgskeleton.subpkg2
??????? ??????? ????????? __init__.py        # Usually empty. Indicates that subpkg1 is a sub-package
??????? ??????? ????????? module1.py
??????? ??????? ????????? module2.py
??????? ????????? topmodule1.py
??????? ????????? topmodule2.py
????????? pypkgskeleton.egg-info/    # Generated by build
??????? ????????? PKG-INFO
??????? ????????? SOURCES.txt
??????? ????????? dependency_links.txt
??????? ????????? top_level.txt
????????? pyproject.toml             # Create this once as shown below
????????? setup.cfg                  # Create this as described below
```

# Create `pyproject.toml`
Create `pyproject.toml` with the following contents.
This just sets up that setuptools will be used to build the package.
```
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

# Create `setup.cfg`
The package name (pypkgskeleton in this example) is the name that is used with `pip`.
The name is the same as the project-level directory and the package's code
directory. All three of these named objects don't necessarily need the same
name, but it's simpler and common to just keep them all the same.

The following is a small subset of the available fields.
For an internal package we don't need most fields, but feel
free to add others (e.g. `license`) if you have a need.
You can omit `description`, `url`, `author`, `author_email`, but it's
best to include them if you can.

The `package = find:` option is a way to tell setuptools to automatically
figure out what packages and sub-packages should be included by looking for
`__init__.py` files in the directory tree
(this is easier than having to explicitly list them).
```
[metadata]
name = pypkgskeleton
version = 0.1.0
description = A short project description
author = Your Name
author_email = your_email@some_domain
url = https://project-home-page

[options]
packages = find:

install_requires =
    pkg1name >= pkg1minversion
    pkg2anyversion
```
(The sample file `setup.cfg` includes a `requests` dependency just as an example.)

You can use `pip freeze` to get a list of packages to include in `install_requires`.
If you have no additional packages, you can omit this option.

# `__init__.py` configuration
See `./pypkgskeleton/__init__.py` for an annotated example `__init__.py` file.
This file may be empty, but the client application import experience can be
improved by providing some additional imports in the `__init__.py` file so that
the caller does not have to.

How the `__init__.py` file is configured affects the client import options.

# Building your package
```
cd <to directory containing setup.cfg>

# Update the version value in setup.cfg
python -m build
```

# Testing your package
For basic testing, you can create a local editable installation using:
`pip install -e .`
This means that as the files change, you don't need to keep re-installing.

To perform a true test, create a new virtual environment in a separate directory
and run:
`pip install --force-reinstall <path to tar.gz file in ./dist directory>`

# Distribute your package
The files in the above `dist` directory can be used by as arguments to `pip` for installation.
Therefore, to distribute your package you can do any of the following:
- Transfer a file from the `dist` directory
- Provide a path to the `dist` directory
- Commit to a git repository

# Installation of your package
(Create a new virtual environment for your consuming application.)

Since we are not using a package manager, use the --force-reinstall to make
sure that you overwrite and install the verison you intend.
```
# For a tar file accessible via a file path:
pip install --force-reinstall <path to pypkgskeleton .tar.gz or .whl file from dist directory>

# For a tar file accessible via git:
pip install --force-reinstall git+<path_to_repo>
pip install --force-reinstall git+ssh://git@gitlab.com/<repo_path>.git@<tag_or_branch>
```
Use `pip list` or `pip freeze` to see what is installed.
Use `pip uninstall pypkgskeleton` to remove the package from the virutal environment.

## AWS Lambda installation
When using you package with a Lambda function, you should either create a Lambda layer
or install the packages locally. To add locally, add the `--upgrade` and `-t .` parameters
to the `pip` command.

# Importing your package
There is a direct connection between what (if anything) you put in your top-level
`__init__.py` file and how the client application imports your objects.
Review the annotated `__init__.py` file to see a variety of examples.

The `dir()` function can be helpful in debugging import configurations. Use `dir()` at the
top level to see what has been imported. To see what has been imported for a given module
or package, use `dir(module or package name)`.
