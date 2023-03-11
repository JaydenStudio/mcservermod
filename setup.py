from distutils.core import setup, Extension
from Cython.Build import cythonize
ext = Extension(name='fib', source=['n.pyx'])
setup(ext_modules=cythonize(ext))