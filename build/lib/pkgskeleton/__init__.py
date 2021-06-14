# These imports are not strictly needed, but including them here
# makes it possible to create aliases (see below) and reduces
# the number of imports that a client app needs to include
import pkgskeleton.topmodule1
import pkgskeleton.topmodule2
import pkgskeleton.subpkg1
import pkgskeleton.subpkg2
import pkgskeleton.subpkg1.module1
import pkgskeleton.subpkg1.module2
import pkgskeleton.subpkg2.module1
import pkgskeleton.subpkg2.module2

##################################################
# Examples of creating aliases for deep modules

# Function/Class level alias examples

# Expose TM2mtest as an alias and therefore allow an import such as:
# from pkgskeleton import TM2mtest
# And then call as:
# TM2mtest()
# Assumes this was included above: import pkgskeleton.topmodule2
from pkgskeleton.topmodule2 import mtest as TM2mtest

# Expose Sub1M1mtest as an alias and therefore allow an import such as:
# from pkgskeleton import Sub1M1mtest
# And then call as:
# Sub1M1mtest()
# Assumes this was included above: import pkgskeleton.subpkg1
# Assumes this was included above: import pkgskeleton.subpkg1.module1
from pkgskeleton.subpkg1.module1 import mtest as Sub1M1mtest

# Module-level alias example

# Expose Sub2M2 as a module-level alias and therefore allow import such as:
# from pkgskeleton import Sub2M2
# And then call as:
# Sub2M2.mtest()
# Assumes this was included above: import pkgskeleton.subpkg2
from pkgskeleton.subpkg2 import module2 as Sub2M2
