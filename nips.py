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
variables = ['eta', 'alpha_homeo', 'eta_homeo', 'l0_sparseness']

variables = ['eta', 'alpha_homeo', 'eta_homeo']

n_jobs = 4 # running in parallel on a multi-core machine
for homeo_method in homeo_methods:
    experiments = SHL_set(dict(homeo_method=homeo_method, datapath=datapath), tag=tag + '_' + homeo_method)
    experiments.run(variables=variables, n_jobs=n_jobs, verbose=1)


for algorithm in ['lasso_lars', 'lasso_cd', 'lars', 'omp', 'mp']: # 'threshold',
    opts = dict(homeo_method='None', learning_algorithm=algorithm, verbose=0)
    shl = SHL(opts)




from CHAMP.DataTools import LocalContrastNormalization, FilterInputData, GenerateMask
from CHAMP.DataLoader import LoadData
import os
home = os.getenv('HOME')
datapath = os.path.join(home, "tmp/database")
path = os.path.join(datapath, "Face_DataBase")
TrSet, TeSet = LoadData('Face', path, decorrelate=False, resize=(65, 65))
to_display = TrSet[0][0, 0:10, :, :, :]
print('Size=', TrSet[0].shape)



TrSet, TeSet = LoadData('Face', path, decorrelate=False, resize=(65, 65))
N_TrSet, _, _, _ = LocalContrastNormalization(TrSet)
Filtered_L_TrSet = FilterInputData(
    N_TrSet, sigma=0.25, style='Custom', start_R=15)


from CHAMP.CHAMP_Layer import CHAMP_Layer
from CHAMP.Monitor import DisplayDico, DisplayConvergenceCHAMP, DisplayWhere

from CHAMP.DataTools import SaveNetwork, LoadNetwork


fname = 'data_cache/CHAMP_high_None.pkl'
try:
    L1_mask = LoadNetwork(loading_path=fname)
except:

    nb_dico = 60
    width = 19
    dico_size = (width, width)
    l0 = 5
    mask = GenerateMask(full_size=(nb_dico, 1, width, width), sigma=0.8, style='Gaussian')
    # Learning Parameters
    eta_homeo = 0.0
    eta = .05
    nb_epoch = 500
    # learn
    L1_mask = CHAMP_Layer(l0_sparseness=l0, nb_dico=nb_dico,
                          dico_size=dico_size, mask=mask, verbose=2)
    dico_mask = L1_mask.TrainLayer(
        Filtered_L_TrSet, eta=eta, eta_homeo=eta_homeo, nb_epoch=nb_epoch, seed=seed)
    SaveNetwork(Network=L1_mask, saving_path=fname)


fname = 'data_cache/CHAMP_low_HAP.pkl'
try:
    L1_mask = LoadNetwork(loading_path=fname)
except:
    # MP Parameters
    nb_dico = 20
    width = 9
    dico_size = (width, width)
    mask = GenerateMask(full_size=(nb_dico, 1, width, width), sigma=0.8, style='Gaussian')
    l0 = 20
    seed = 30
    # Learning Parameters
    eta = .05
    nb_epoch = 500

    # Learning Parameters
    eta_homeo = 0.0025
    L1_mask = CHAMP_Layer(l0_sparseness=l0, nb_dico=nb_dico,
                          dico_size=dico_size, mask=mask, verbose=1)
    dico_mask = L1_mask.TrainLayer(
        Filtered_L_TrSet, eta=eta, eta_homeo=eta_homeo, nb_epoch=nb_epoch, seed=seed)
    SaveNetwork(Network=L1_mask, saving_path=fname)


fname = 'data_cache/CHAMP_low_None.pkl'
try:
    L1_mask = LoadNetwork(loading_path=fname)
except:
    # MP Parameters
    nb_dico = 20
    width = 9
    dico_size = (width, width)
    mask = GenerateMask(full_size=(nb_dico, 1, width, width), sigma=0.8, style='Gaussian')
    l0 = 20
    seed = 30
    # Learning Parameters
    eta = .05
    nb_epoch = 500


    L1_mask = CHAMP_Layer(l0_sparseness=l0, nb_dico=nb_dico,
                      dico_size=dico_size, mask=mask, verbose=2)
    dico_mask = L1_mask.TrainLayer(
        Filtered_L_TrSet, eta=eta, nb_epoch=nb_epoch, seed=seed)
    SaveNetwork(Network=L1_mask, saving_path=fname)


fname = 'data_cache/CHAMP_high_HAP.pkl'
try:
    L1_mask = LoadNetwork(loading_path=fname)
except:

    nb_dico = 60
    width = 19
    dico_size = (width, width)
    l0 = 5
    mask = GenerateMask(full_size=(nb_dico, 1, width, width), sigma=0.8, style='Gaussian')
    # Learning Parameters
    eta_homeo = 0.0025
    eta = .05
    nb_epoch = 500
    # learn
    L1_mask = CHAMP_Layer(l0_sparseness=l0, nb_dico=nb_dico,
                          dico_size=dico_size, mask=mask, verbose=2)
    dico_mask = L1_mask.TrainLayer(
        Filtered_L_TrSet, eta=eta, eta_homeo=eta_homeo, nb_epoch=nb_epoch, seed=seed)
    SaveNetwork(Network=L1_mask, saving_path=fname)



fname = 'data_cache/CHAMP_MNIST_HAP.pkl'
try:
    L1_mask = LoadNetwork(loading_path=fname)
except:

    path = os.path.join(datapath, "MNISTtorch")

    TrSet, TeSet = LoadData('MNIST', data_path=path)
    N_TrSet, _, _, _ = LocalContrastNormalization(TrSet)
    Filtered_L_TrSet = FilterInputData(
        N_TrSet, sigma=0.25, style='Custom', start_R=15)


    nb_dico = 60
    width = 7
    dico_size = (width, width)
    l0 = 15
    mask = GenerateMask(full_size=(nb_dico, 1, width, width), sigma=0.8, style='Gaussian')
    # Learning Parameters
    eta_homeo = 0.0025
    eta = .05
    nb_epoch = 500
    # learn
    L1_mask = CHAMP_Layer(l0_sparseness=l0, nb_dico=nb_dico,
                          dico_size=dico_size, mask=mask, verbose=2)
    dico_mask = L1_mask.TrainLayer(
        Filtered_L_TrSet, eta=eta, eta_homeo=eta_homeo, nb_epoch=nb_epoch, seed=seed)
    SaveNetwork(Network=L1_mask, saving_path=fname)