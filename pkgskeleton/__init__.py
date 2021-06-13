# TODO annotate this more...
import pkgskeleton.topmodule1
import pkgskeleton.topmodule2
import pkgskeleton.subpkg1.module1
import pkgskeleton.subpkg1.module2
import pkgskeleton.subpkg2.module1
import pkgskeleton.subpkg2.module2
from pkgskeleton.subpkg1.module1 import mtest as s1m1_mtest

# Then in client, use this way
# from pkgskeleton import s1m1_mtest
# s1m1_mtest()

