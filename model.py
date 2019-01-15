#!/usr/bin/env python3
# -*- coding: utf-8 -*
tag = 'IJCNN'
from shl_scripts.shl_experiments import SHL, prun
# pre-loading data
datapath = '../../SparseHebbianLearning/database'
opts = dict(datapath=datapath, verbose=0)

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
    n_jobs = int(sys.argv[1])
    print('n_jobs=', n_jobs)
except:
    n_jobs = 4
    n_jobs = 9
    n_jobs = 10
    n_jobs = 1
    n_jobs = 35

    
if n_jobs>0:
    # Figure 1 & 3

    list_figures = []

    from shl_scripts.shl_experiments import SHL_set
    for homeo_method in homeo_methods:
        opts_ = opts.copy()
        opts_.update(homeo_method=homeo_method)
        experiments = SHL_set(opts_, tag=tag + '_' + homeo_method, N_scan=N_cv)
        experiments.run(variables=['seed'], n_jobs=n_jobs, verbose=0)

    # Figure 2-B
    variables = ['eta', 'eta_homeo']

    list_figures = []
    for homeo_method in homeo_methods:
        opts_ = opts.copy()
        opts_.update(homeo_method=homeo_method)
        experiments = SHL_set(opts_, tag=tag + '_' + homeo_method, base=10)
        experiments.run(variables=variables, n_jobs=n_jobs, verbose=0)



    # Annex X.X

    shl = SHL(**opts)
    dico = shl.learn_dico(data=data, list_figures=list_figures, matname=tag + '_vanilla')

    
    variables = ['alpha_homeo', 'l0_sparseness', 'n_dictionary']
    bases = [4] * len(variables)

    for homeo_method, base in zip(homeo_methods, bases):
        opts_ = opts.copy()
        opts_.update(homeo_method=homeo_method)
        experiments = SHL_set(opts_, tag=tag + '_' + homeo_method, base=base)
        experiments.run(variables=variables, n_jobs=n_jobs, verbose=0)

    for algorithm in ['lasso_lars', 'lasso_cd', 'lars', 'elastic', 'omp', 'mp']: # 'threshold',
        opts_ = opts.copy()
        opts_.update(homeo_method='None', learning_algorithm=algorithm, verbose=0)
        shl = SHL(**opts_)
        dico= shl.learn_dico(data=data, list_figures=[],
                       matname=tag + ' - algorithm={}'.format(algorithm))

    for homeo_method in ['None', 'HAP']:
        for algorithm in ['lasso_lars', 'lars', 'elastic', 'omp', 'mp']: # 'threshold', 'lasso_cd', 
            opts_ = opts.copy()
            opts_.update(homeo_method=homeo_method, learning_algorithm=algorithm, verbose=0)
            shl = SHL(**opts_)
            dico= shl.learn_dico(data=data, list_figures=[],
                           matname=tag + ' - algorithm={}'.format(algorithm) + ' - homeo_method={}'.format(homeo_method))
    
    shl = SHL(one_over_F=False, **opts)
    dico_w = shl.learn_dico(data=data, matname=tag + '_WHITE', list_figures=[])
    shl = SHL(one_over_F=True, **opts)
    dico_1oF = shl.learn_dico(data=data, matname=tag + '_OVF', list_figures=[])

    shl = SHL(beta1=0., **opts)
    dico_fixed = shl.learn_dico(data=data, matname=tag + '_fixed', list_figures=[])
    shl = SHL(**opts)
    dico_default = shl.learn_dico(data=data, matname=tag + '_default', list_figures=[])
