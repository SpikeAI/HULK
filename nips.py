#!/usr/bin/env python3
# -*- coding: utf-8 -*
from shl_scripts.shl_experiments import SHL

# pre-loading data
datapath = '../../SHL_master/database'
shl = SHL(datapath=datapath)
data = shl.get_data(matname='data')

tag = 'NIPS'
shl = SHL(eta=0.01, beta1=0.)
dico_fixed = shl.learn_dico(data=data, matname=tag + '_fixed', list_figures=[])
shl = SHL()
dico_default = shl.learn_dico(data=data, matname=tag + '_default', list_figures=[])



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
variables = ['eta', 'alpha_homeo', 'eta_homeo', 'l0_sparseness']

variables = ['eta', 'alpha_homeo', 'eta_homeo']

n_jobs = 18 # running in parallel on a multi-core machine
for homeo_method in homeo_methods:
    experiments = SHL_set(dict(homeo_method=homeo_method, datapath=datapath), tag=tag + '_' + homeo_method)
    experiments.run(variables=variables, n_jobs=n_jobs, verbose=0)


for algorithm in ['lasso_lars', 'lasso_cd', 'lars', 'omp', 'mp']: # 'threshold',
    opts = dict(homeo_method='None', learning_algorithm=algorithm, verbose=0)
    shl = SHL(opts)
    dico= shl.learn_dico(data=data, list_figures=[],
                   matname=tag + ' - algorithm={}'.format(algorithm))

shl = SHL(one_over_F=True)
dico_1oF = shl.learn_dico(data=data, matname=tag + '_OVF', list_figures=[])
