tag = 'NIPS'
from shl_scripts.shl_experiments import SHL
N_cv = 10
homeo_methods = ['None', 'OLS', 'HEH', 'HAP', 'EMP']
seed = 42

list_figures = []
for i_cv in range(N_cv):
    for homeo_method in homeo_methods:
        shl = SHL(homeo_method=homeo_method, seed=seed+i_cv)
        shl.learn_dico(data=shl.get_data(matname=tag + '_test'), list_figures=list_figures, matname=tag + '_' + homeo_method + '_' + str(i_cv))
