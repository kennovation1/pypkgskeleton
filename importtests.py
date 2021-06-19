# Example imports and use of package that will work
# even if package __init__.py files are empty.

# Use function defined in a top module
import pypkgskeleton.topmodule2
pypkgskeleton.topmodule2.mtest()
# Prints: This is pypkgskeleton.topmodule2

# Same as above, but using 'from' to save some typing in the function call
from pypkgskeleton import topmodule1
topmodule1.mtest()
# Prints: This is pypkgskeleton.topmodule1

# Access function in a module in a sub-package
import pypkgskeleton.subpkg1.module1
pypkgskeleton.subpkg1.module1.mtest()
# Prints: This is pypkgseleton.subpkg1.module1

###########################################################

# To make imports a little cleaner, we can add some imports
# to the top-level __init__.py file to create aliases and then
# then we can use these aliases as follows.
# See the __init__.py file to see how to create these aliases.

# Use function defined in a top module
from pypkgskeleton import TM2mtest
TM2mtest()
# Prints: This is pypkgskeleton.topmodule2

# Use function defined in a module in a sub-package
from pypkgskeleton import Sub1M1mtest
Sub1M1mtest()
# Prints: This is pypkgseleton.subpkg1.module1

# Use a module-level alias
from pypkgskeleton import Sub2M2
Sub2M2.mtest()