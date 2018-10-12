#!/usr/bin/env python3
# -*- coding: utf-8 -*
tag = 'ICLR'
from shl_scripts.shl_experiments import SHL, prun
# pre-loading data
datapath = '../../SparseHebbianLearning/database'
# different runs
#opts = dict(eta=0.007, eta_homeo=0.02, alpha_homeo=.5, cache_dir='cache_dir_1100', datapath=datapath) 
#opts = dict(eta=0.007, eta_homeo=0.02, alpha_homeo=.08, cache_dir='cache_dir_1900', datapath=datapath) 
#opts = dict(eta=0.007, eta_homeo=0.005, alpha_homeo=5., cache_dir='cache_dir_1700', datapath=datapath)
#opts = dict(eta=0.0033, eta_homeo=0.05, alpha_homeo=.5, cache_dir='cache_dir_frioul', datapath=datapath)
#opts = dict(eta=0.007, eta_homeo=0.005, alpha_homeo=5., cache_dir='cache_dir', datapath=datapath)
#opts = dict(eta=0.0033, eta_homeo=0.05, alpha_homeo=2.5, cache_dir='cache_dir_42', datapath=datapath, verbose=0)
opts = dict(eta=0.005, eta_homeo=0.005, alpha_homeo=2.5, cache_dir='cache_dir', datapath=datapath, verbose=0)
shl = SHL(**opts)
data = shl.get_data(matname=tag)

# running main simulations
# Figure 1 & 3
N_cv = 10
homeo_methods = ['None', 'OLS', 'HEH', 'HAP', 'EMP']
seed = 42

# running in parallel on a multi-core machine
import sys
try:
    n_jobs = sys.argv[2]
except:
    n_jobs = 4
    n_jobs = 9
    n_jobs = 10
    n_jobs = 35
    n_jobs = 1

list_figures = []

from shl_scripts.shl_experiments import SHL_set
for homeo_method in homeo_methods:
    opts_ = opts.copy()
    opts_.update(homeo_method=homeo_method)
    experiments = SHL_set(opts_, tag=tag + '_' + homeo_method, N_scan=N_cv)
    experiments.run(variables=['seed'], n_jobs=n_jobs, verbose=0)

# Figure 2-B
variables = ['eta', 'alpha_homeo', 'eta_homeo', 'l0_sparseness']

variables = ['eta', 'alpha_homeo', 'eta_homeo']

for homeo_method in homeo_methods:
    opts_ = opts.copy()
    opts_.update(homeo_method=homeo_method)
    experiments = SHL_set(opts_, tag=tag + '_' + homeo_method)
    experiments.run(variables=variables, n_jobs=n_jobs, verbose=0)

# Annex X.X
for algorithm in ['lasso_lars', 'lasso_cd', 'lars', 'omp', 'mp']: # 'threshold',
    opts_ = opts.copy()
    opts_.update(homeo_method='None', learning_algorithm=algorithm, verbose=0)
    shl = SHL(**opts_)
    dico= shl.learn_dico(data=data, list_figures=[],
                   matname=tag + ' - algorithm={}'.format(algorithm))
