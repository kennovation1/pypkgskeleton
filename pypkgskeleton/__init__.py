# These imports are not strictly needed, but including them here
# makes it possible to create aliases (see below) and reduces
# the number of imports that a client app needs to include
import pypkgskeleton.topmodule1
import pypkgskeleton.topmodule2
import pypkgskeleton.subpkg1
import pypkgskeleton.subpkg2
import pypkgskeleton.subpkg1.module1
import pypkgskeleton.subpkg1.module2
import pypkgskeleton.subpkg2.module1
import pypkgskeleton.subpkg2.module2

##################################################
# Examples of creating aliases for deep modules

# NOTE: Do not name a top module to be the same as the package name.
# For example having a top module called pypkgskeleton.py in the
# pypkgskeleton package will cause an import error.

# Elevate all of topmodule1 to the client so that objects may be imported as
# from pypkgskeleton import <something defined in topmodule1>

# Function/Class level alias examples

# Expose TM2mtest as an alias and therefore allow an import such as:
# from pypkgskeleton import TM2mtest
# And then call as:
# TM2mtest()
# Assumes this was included above: import pypkgskeleton.topmodule2
from pypkgskeleton.topmodule2 import mtest as TM2mtest

# Expose Sub1M1mtest as an alias and therefore allow an import such as:
# from pypkgskeleton import Sub1M1mtest
# And then call as:
# Sub1M1mtest()
# Assumes this was included above: import pypkgskeleton.subpkg1
# Assumes this was included above: import pypkgskeleton.subpkg1.module1
from pypkgskeleton.subpkg1.module1 import mtest as Sub1M1mtest

# Module-level alias example

# Expose Sub2M2 as a module-level alias and therefore allow import such as:
# from pypkgskeleton import Sub2M2
# And then call as:
# Sub2M2.mtest()
# Assumes this was included above: import pypkgskeleton.subpkg2
from pypkgskeleton.subpkg2 import module2 as Sub2M2
