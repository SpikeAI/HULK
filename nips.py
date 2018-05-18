#!/usr/bin/env python3
# -*- coding: utf-8 -*
from shl_scripts.shl_experiments import SHL

# pre-loading data
datapath = '../../SHL_master/database'
shl = SHL(datapath=datapath)
data = shl.get_data(matname='data')

tag = 'NIPS'
# Figure 1 & 3
N_cv = 10
homeo_methods = ['None', 'OLS', 'HEH', 'HAP', 'EMP']
seed = 42

list_figures = []
for i_cv in range(N_cv):
    for homeo_method in homeo_methods:
        shl = SHL(homeo_method=homeo_method, seed=seed+i_cv)
        shl.learn_dico(data=data, list_figures=list_figures, matname=tag + '_' + homeo_method + '_' + str(i_cv))

# Figure 2-B
from shl_scripts.shl_experiments import SHL_set
variables = ['eta', 'alpha_homeo', 'eta_homeo']

n_jobs = 2 # running in parallel on a multi-core machine
for homeo_method in homeo_methods:
    experiments = SHL_set(dict(homeo_method=homeo_method, datapath=datapath), tag=tag + '_' + homeo_method)
    experiments.run(variables=variables, n_jobs=n_jobs)