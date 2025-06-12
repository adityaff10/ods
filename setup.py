from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy
import os
import importlib.util

# Load the version dynamically using importlib
version_file = os.path.join('.', 'darkflow', 'version.py')
spec = importlib.util.spec_from_file_location("version", version_file)
version_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version_module)
VERSION = version_module.__version__

# Define extension modules for different OS
if os.name == 'nt':
    ext_modules = [
        Extension("darkflow.cython_utils.nms",
            sources=["darkflow/cython_utils/nms.pyx"],
            include_dirs=[numpy.get_include()]
        ),
        Extension("darkflow.cython_utils.cy_yolo2_findboxes",
            sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],
            include_dirs=[numpy.get_include()]
        ),
        Extension("darkflow.cython_utils.cy_yolo_findboxes",
            sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],
            include_dirs=[numpy.get_include()]
        )
    ]
elif os.name == 'posix':
    ext_modules = [
        Extension("darkflow.cython_utils.nms",
            sources=["darkflow/cython_utils/nms.pyx"],
            libraries=["m"],  # Unix-like specific
            include_dirs=[numpy.get_include()]
        ),
        Extension("darkflow.cython_utils.cy_yolo2_findboxes",
            sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],
            libraries=["m"],  # Unix-like specific
            include_dirs=[numpy.get_include()]
        ),
        Extension("darkflow.cython_utils.cy_yolo_findboxes",
            sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],
            libraries=["m"],  # Unix-like specific
            include_dirs=[numpy.get_include()]
        )
    ]
else:
    ext_modules = [
        Extension("darkflow.cython_utils.nms",
            sources=["darkflow/cython_utils/nms.pyx"],
            libraries=["m"]  # Unix-like specific
        ),
        Extension("darkflow.cython_utils.cy_yolo2_findboxes",
            sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],
            libraries=["m"]  # Unix-like specific
        ),
        Extension("darkflow.cython_utils.cy_yolo_findboxes",
            sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],
            libraries=["m"]  # Unix-like specific
        )
    ]

setup(
    version=VERSION,
    name='darkflow',
    description='Darkflow',
    license='GPLv3',
    url='https://github.com/thtrieu/darkflow',
    packages=find_packages(),
    scripts=['flow'],
    ext_modules=cythonize(ext_modules)
)
