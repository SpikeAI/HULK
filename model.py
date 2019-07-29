# running in parallel on a multi-core machine
import sys

try:
    tag = sys.argv[1]
except:
    tag = 'HULK'

print('tag =', tag)

try:
    n_jobs = int(sys.argv[2])
except:
    n_jobs = 4
    n_jobs = 9
    n_jobs = 10
    n_jobs = 1
    n_jobs = 35
    n_jobs = 0

print('n_jobs =', n_jobs)

from shl_scripts.shl_experiments import SHL, prun
# pre-loading data
datapath = '../SparseHebbianLearning/database'
opts = dict(datapath=datapath, verbose=0)

shl = SHL(**opts)
data = shl.get_data(matname=tag)

# running main simulations
# Figure 1 & 3
N_cv = 10 # cross-validate with 10 different learnings
homeo_methods = ['None', 'OLS', 'HEH', 'HAP', 'EMP']
seed = 42

import numpy as np
np.set_printoptions(precision=2, suppress=True)
np.random.seed(seed)

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

else:
    # some overhead for the formatting of figures
    import matplotlib.pyplot as plt

    fontsize = 12
    FORMATS = ['.pdf', '.eps', '.png', '.tiff']
    FORMATS = ['.pdf', '.png']
    dpi_export = 600

    fig_width_pt = 318.670  # Get this from LaTeX using \showthe\columnwidth
    fig_width_pt = 450  # Get this from LaTeX using \showthe\columnwidth
    #fig_width_pt = 1024 #221     # Get this from LaTeX using \showthe\columnwidth / x264 asks for a multiple of 2
    ppi = 72.27 # (constant) definition of the ppi = points per inch
    inches_per_pt = 1.0/ppi  # Convert pt to inches
    #inches_per_cm = 1./2.54
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    grid_fig_width = 2*fig_width
    phi = (np.sqrt(5) + 1. ) /2
    #legend.fontsize = 8
    #fig_width = 9
    fig_height = fig_width/phi
    figsize = (fig_width, fig_height)


    def adjust_spines(ax, spines):
        for loc, spine in ax.spines.items():
            if loc in spines:
                spine.set_position(('outward', 10))  # outward by 10 points
                spine.set_smart_bounds(True)
            else:
                spine.set_color('none')  # don't draw spine

        # turn off ticks where there is no spine
        if 'left' in spines:
            ax.yaxis.set_ticks_position('left')
        else:
            # no yaxis ticks
            ax.yaxis.set_ticks([])

        if 'bottom' in spines:
            ax.xaxis.set_ticks_position('bottom')
        else:
            # no xaxis ticks
            ax.xaxis.set_ticks([])

    import matplotlib
    pylab_defaults = {
        'font.size': 10,
        'xtick.labelsize':'medium',
        'ytick.labelsize':'medium',
        'text.usetex': False,
        'font.family' : 'sans-serif',
        'font.sans-serif' : ['DejaVu Sans'],#['Optima'],#['Palatino'],#
        }

    #matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
    matplotlib.rcParams.update(pylab_defaults)
    #matplotlib.rcParams.update({'text.usetex': True})

    import matplotlib.cm as cm


    from IPython.display import Image

    DEBUG = True
    DEBUG = False
    hl, hs = 10*'-', 10*' '
