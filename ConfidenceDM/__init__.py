#!/usr/bin/python
#-*- coding: UTF-8 -*-
"""
Full package related to the publication ...

Author: Luciano Paz
Year: 2018

"""

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

__version__ = '1.1'

from . import data_io
from . import decision_model
from . import fits_module
from . import utils
from .data_io import (SubjectSession, unique_subject_sessions,
                      anonimize_subjects, filter_subjects_list,
                      merge_subjectSessions, increase_histogram_count,
                      compute_roc, compute_auc)
from .decision_model import DecisionModel, diffusion_path_samples, sim_rt
from .fits_module import (load_Fitter_from_file, Fitter_filename, Fitter,
                          Fitter_plot_handler, parse_input, prepare_fit_args)
