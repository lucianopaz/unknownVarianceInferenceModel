#!/usr/bin/python
#-*- coding: UTF-8 -*-
"""
Setup script for the leakyIntegrator package related to the publication ...
It involves the use of a Makefile during the build phase, and it does so
by calling subprocess.Popen with shell=True. This means that you must
trust this source not to have been tampered with, or install without sudo.
For a more detailed explanation of why the build_ext class was overloaded
refer to https://stackoverflow.com/a/48641638/7253166

Author: Luciano Paz
Year: 2018

"""

import os, subprocess, codecs, re, platform
import setuptools
from setuptools.command.build_ext import build_ext
from distutils.errors import DistutilsSetupError
from distutils import log as distutils_logger



extension1 = setuptools.extension.Extension('ConfidenceDM.dmmodule',
                    sources = ['ConfidenceDM/src/decision_model.cpp',
                               'ConfidenceDM/src/dmmodule.cpp'],
                    extra_compile_args = ['-Wno-write-strings','-O2']
                    )


class build_ext_numpy(build_ext, object):
    def finalize_options(self):
        # The reason for this is the need to get numpy include and
        # library dirs but numpy could a priori not be available! This
        # means that you need to bootstrap numpy's installation.
        # This hackish solution was taken from
        # https://stackoverflow.com/a/21621689/7253166
        
        
        super(build_ext_numpy, self).finalize_options()
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())

here = os.path.abspath(os.path.dirname(__file__))
def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setuptools.setup(name = 'ConfidenceDM',
                 version = find_version('ConfidenceDM', '__init__.py'),
                 description = 'Methods to compute the decision bounds and '
                               'joint response time and confidence '
                               'distributions for bayesian inference',
                 ext_modules = [extension1],
                 cmdclass = {'build_ext': build_ext_numpy},
                 setup_requires=['numpy>=1.13'],
                 install_requires = ['matplotlib>=2',
                                     'numpy>=1.13',
                                     'scipy>=1',
                                     'six',
                                     'cma>=2.5',
                                     'enum',
                                    ],
                 # metadata for upload to PyPI
                 author="Luciano Paz",
                 author_email="lpaz@sissa.it",
                 license="MIT",
                 url="https://github.com/lucianopaz/"
                     "unknownVarianceInferenceModel",
                )
