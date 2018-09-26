#!/usr/bin/env python3
# -*- coding: utf-8 -*
from shl_scripts.shl_experiments import SHL, prun
# pre-loading data
datapath = '../../SparseHebbianLearning/database'
opts = dict(datapath=datapath, verbose=0)

shl = SHL(**opts)
data = shl.get_data(matname='data')

tag = 'ICLR'
# Figure 1 & 3
N_cv = 10
homeo_methods = ['None', 'OLS', 'HEH', 'HAP', 'EMP']
seed = 42

# running in parallel on a multi-core machine
n_jobs = 8
n_jobs = 35

list_figures = []

from shl_scripts.shl_experiments import SHL_set
for homeo_method in homeo_methods:
    experiments = SHL_set(dict(homeo_method=homeo_method, datapath=datapath), tag=tag + '_' + homeo_method, N_scan=N_cv)
    experiments.run(variables='seed', n_jobs=n_jobs, verbose=0)

# Figure 2-B
variables = ['eta', 'alpha_homeo', 'eta_homeo', 'l0_sparseness']

variables = ['eta', 'alpha_homeo', 'eta_homeo']

for homeo_method in homeo_methods:
    experiments = SHL_set(dict(homeo_method=homeo_method, datapath=datapath), tag=tag + '_' + homeo_method)
    experiments.run(variables=variables, n_jobs=n_jobs, verbose=0)

# Annex X.X
for algorithm in ['lasso_lars', 'lasso_cd', 'lars', 'omp', 'mp']: # 'threshold',
    opts = dict(homeo_method='None', learning_algorithm=algorithm, verbose=0)
    shl = SHL(opts)
    dico= shl.learn_dico(data=data, list_figures=[],
                   matname=tag + ' - algorithm={}'.format(algorithm))