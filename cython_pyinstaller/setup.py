from setuptools import find_packages, setup
from setuptools.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext
import os
import numpy

def rmdirs(path):
    for root, dirs, files in os.walk(path):
        for currentFile in files:
            exts = ('.pyd', '.exp', ".lib", ".c")
            if currentFile.lower().endswith(exts):
                os.remove(os.path.join(root, currentFile))
rmdirs(os.getcwd())

substrings = ["substring_to_exclude",]

def scandir(dir, files=[]):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if  os.path.isfile(path) and path.endswith(".py") and not any(substring in path for substring in substrings):
            files.append(path.replace(os.path.sep, ".")[:-3])
        elif os.path.isdir(path):
            scandir(path, files)
    return files

def makeExtension(extName):
    extPath = extName.replace(".", os.path.sep)+".py"
    return Extension(
        extName,
        [extPath],
        include_dirs = [numpy.get_include(), "."],
        extra_compile_args = ["-O3", "-Wall"],
        )

modules = ["packages", 
           ]
ls_extensions = []
for module in modules:
    extNames = scandir(module)
    ls_extensions+=[makeExtension(name) for name in extNames]

setup(
    name="app",
    version='1.0',
    ext_modules = cythonize(
        ls_extensions,
        build_dir="build_cythonize",
        compiler_directives={
            'language_level' : "3",
            'always_allow_keywords': True,
        }
    ),
    cmdclass=dict(
        build_ext=build_ext
    ),
)