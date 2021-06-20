'''
# These imports are not strictly needed, but some or all of them
# here reduce the imports required by the client app.
# This is mostly useful for deep modules.
# TODO: There's room for improvement to explain when these are
# helpful and show examples
import pypkgskeleton.topmodule1
import pypkgskeleton.topmodule2
import pypkgskeleton.subpkg1
import pypkgskeleton.subpkg2
import pypkgskeleton.subpkg1.module1
import pypkgskeleton.subpkg1.module2
import pypkgskeleton.subpkg2.module1
import pypkgskeleton.subpkg2.module2

##################################################

# Elevate all of topmodule1 to the client
# Usage:
# from pypkgskeleton import <something defined in topmodule1>
# from pypkgskeleton import mtest
# mtest()
from pypkgskeleton.topmodule1 import *

# As above, but just expose specific objects instead of all
# Usage:
# from pypkgskeleton import mtest
# mtest()
from pypkgskeleton.topmodule2 import mtest

# Since mtest is defined in both top modules, we might want to use an alias
# Usage:
# from pypkgskeleton import TM2mtest
# TM2mtest()
from pypkgskeleton.topmodule2 import mtest as TM2mtest

# Example of pulling a deeper module to the top
# Usage:
# from pypkgskeleton import Sub1M1mtest
# Sub1M1mtest()
from pypkgskeleton.subpkg1.module1 import mtest as Sub1M1mtest

# You can also expose a deep module by aliasing it to the top
# Usage:
# from pypkgskeleton import Sub2M2
# Sub2M2.mtest()
from pypkgskeleton.subpkg2 import module2 as Sub2M2
'''