import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
#import pyreadr
import pandas as pd
class sier_c:
    
    def abc(self,N_k,first_infections,days,OD):
            locs_len = len(N_k)                 # number of locations
            #print(locs_len)
            SIER = np.zeros(shape=(locs_len, 4)) # make a numpy array with 3 columns for keeping track of the S, I, R groups
            SIER[:,0] = N_k                      # initialize the S group with the respective populations
            
            #first_infections = np.full(locs_len,0)   # for demo purposes, randomly introduce infections

            np.seterr(divide='ignore', invalid='ignore')
            SIER[:, 0] = SIER[:, 0] - first_infections
            SIER[:, 1] = SIER[:, 1] + first_infections                           # move infections to the I group
            
            # row normalize the SIR matrix for keeping track of group proportions
            row_sums = SIER.sum(axis=1)
            self.k=row_sums[:, np.newaxis]
            SIER_n = SIER / self.k
            SIER_n=np.where(np.isnan(SIER_n),0,SIER_n)
            #print(SIER)
            # initialize parameters
            beta = 0.3
            gamma = 0.1
            sigma = 0.2                                 # alpha
            #R0 = beta/gamma
            beta_vec = np.full(locs_len, beta)
            gamma_vec = np.full(locs_len, gamma)
            sigma_vec = np.full(locs_len, sigma)
            #public_trans_vec = np.full(locs_len, public_trans)
            
            # make copy of the SIR matrices 
            SIER_sim = SIER.copy()
            SIER_nsim = SIER_n.copy()
            
            # run model
            #print("lem",len(SIER_sim))
            #from tqdm import tqdm_notebook
            infected_pop_norm = []
            susceptible_pop_norm = []
            recovered_pop_norm = []
            exp_pop_norm=[]
            S = SIER_sim[:,0].sum()/N_k.sum()
            I = SIER_sim[:,1].sum()/N_k.sum()
            E = SIER_sim[:,2].sum()/N_k.sum()
            R = SIER_sim[:,3].sum()/N_k.sum()
            print(S, I,E, R)
            
    #print('\n')
            infected_pop_norm.append(I)
            susceptible_pop_norm.append(S)
            exp_pop_norm.append(E)
            recovered_pop_norm.append(R)
            for i in range(0,days):
                infected_mat = np.repeat([SIER_nsim[:,1],],repeats=3774,axis=0)
                
                #infected_mat = np.array([SIER_nsim[:,1],]*locs_len).transpose()
                OD_infected =np.round (OD*infected_mat)
                OD_infected=np.where(np.isnan(OD_infected),0,OD_infected)
                inflow_infected = OD_infected.sum(axis=0)
                #inflow_infected = np.round(inflow_infected*sigma_vec)
                #print('total infected inflow: ', inflow_infected.sum(),"\t",inflow_infected)
                self.t= (N_k + OD.sum(axis=0)) + (beta_vec * SIER_sim[:, 0] * SIER_sim[:, 1] / N_k)
                new_exposed = beta_vec * SIER_sim[:, 0] * inflow_infected /(N_k + OD.sum(axis=0)) + (beta_vec * SIER_sim[:, 0] * SIER_sim[:, 1] / N_k)
                new_exposed=np.where(np.isnan(new_exposed),0,new_exposed)
                new_infect = sigma_vec * SIER_sim[:, 2]
                new_infect=np.where(np.isnan(new_infect),0,new_infect)
                new_recovered = gamma_vec*SIER_sim[:, 1]
                new_recovered=np.where(np.isnan(new_recovered),0,new_recovered)
                new_infect = np.where(new_infect>SIER_sim[:, 0], SIER_sim[:, 0], new_infect)
                #S
                SIER_sim[:, 0] = SIER_sim[:, 0] - new_exposed
                #I
                SIER_sim[:, 1] = SIER_sim[:, 1] + new_infect - new_recovered
                #E  
                SIER_sim[:, 2] = SIER_sim[:, 2] + new_exposed - new_recovered
                #R
                SIER_sim[:, 3] = SIER_sim[:, 3] + new_recovered
                                                                
                
                                                                
                SIER_sim = np.where(SIER_sim<0,0,SIER_sim)
                # recompute the normalized SIR matrix

                row_sums = SIER_sim.sum(axis=1)
                self.m = row_sums[:, np.newaxis]
                SIER_nsim = SIER_sim / self.m
                S = SIER_sim[:,0].sum()/N_k.sum()
                I = SIER_sim[:,1].sum()/N_k.sum()
                E = SIER_sim[:,2].sum()/N_k.sum()
                R = SIER_sim[:,3].sum()/N_k.sum()
                #print(S, I,E, R)
                #print('\n')
                infected_pop_norm.append(I)
                susceptible_pop_norm.append(S)
                exp_pop_norm.append(E)
                recovered_pop_norm.append(R)
            return self,infected_pop_norm,susceptible_pop_norm,exp_pop_norm,recovered_pop_norm
