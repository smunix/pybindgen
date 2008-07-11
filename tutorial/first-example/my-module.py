import pybindgen
import sys

mod = pybindgen.Module('MyModule')
mod.add_include('"my-module.h"')
mod.add_function('MyModuleDoAction', None, [])
mod.generate(sys.stdout)
