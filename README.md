Testing using this guide: https://changhsinlee.com/python-package/

The top `lunch_options` is the project folder and the child `lunch_options`
is the source code folder.


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

# Setup
You you do all of the following in a Python virtual environment.
Describing virtual environments is beyond the scope of this project.
I'll assume you are using Python 3.7 or greater.

## One time installation of build tools
```
pip install -q build
```

# Directory structure
Here is our directory structure. This example shows top-level modules in the
package root and two sub-packages, each with multiple modules.

You can delete one or both subpackages or add more.
You can have one or more modules in the root package.

Below, we'll look at configuring `__init__.py` to show different ways
of allowing the client program to more easily import modules.

**TODO** refresh this
```
pkgskeleton/
├── README.md
├── pkgskeleton/         <- Our root package: import pkgskeleton
│   ├── __init__.py
│   ├── subpkg1/         <- A sub-package: import pkgskeleton.subpkg1
│   │   ├── __init__.py
│   │   ├── module1.py
│   │   └── module2.py
│   ├── subpkg2/
│   │   ├── __init__.py  <- A sub-package: import pkgskeleton.subpkg2
│   │   ├── module1.py
│   │   └── module2.py
│   ├── topmodule1.py
│   └── topmodule2.py
└── setup.py
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
The package name (pkgskeleton) is the name that is used with `pip`.
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
name = pkgskeleton
version = 0.1.1
description = A short project description
author = Your Name
author_email = your_email@some_domain
url = https://project-home-page

[options]
packages = find:
```

# `__init__.py` configuration
**TODO**

# Building your package
There are ways of building and testing your packaging in an iterative
fashion. However, to keep things simple, we're going to skip that and
just let you build/deploy/test in a way that assume that you'll not do
this often and therefore do not need to optimize the process.
```
cd <to directory containing setup.py>
# Update the version value in setup.py
python -m build
```

# Distribute your package
**TODO**

# Installation of your package
Since we are not using a package manager, use the --force-reinstall to make
sure that you overwrite and install the verison you intend.
```
# For a tar file accessible via a file path:
pip install --force-reinstall <path to pkgskeleton dist/ .tar.gz file>

# For a tar file accessible via git:
pip install --force-reinstall git+<path to pkgskeleton dist/ .tar.gz file>
```

# Importing your package
**TODO**
