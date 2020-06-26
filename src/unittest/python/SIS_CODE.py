import matplotlib

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
#import pyreadr
import pandas as pd
class sis_c:
    def abc(self,N_k,first_infections,days,OD,beta,gamma,transmission_probability,contact_rate):
            # initialize the population vector from the origin-destination flow matrix
            #OD=np.array([[10,12,3,5],[3,3,45,6],[3,2,4,5],[5,6,5,3]])
            #N_k =np.array([100,23,456,454])
            
            locs_len = len(N_k)                 # number of locations
            #print(locs_len)
            SIS = np.zeros(shape=(locs_len, 2)) # make a numpy array with 3 columns for keeping track of the S, I, R groups
            SIS[:,0] = N_k                      # initialize the S group with the respective populations
            np.seterr(divide='ignore', invalid='ignore')
            #first_infections = [1,2,4,5]  # for demo purposes, randomly introduce infections
            #print(sum(first_infections))
            SIS[:, 0] = SIS[:, 0] - first_infections
            SIS[:, 1] = SIS[:, 1] + first_infections                           # move infections to the I group
            #print(SIS)
            # row normalize the SIS matrix for keeping track of group proportions
            row_sums = SIS.sum(axis=1)
            self.t=row_sums[:, np.newaxis]
            SIS_n = SIS / row_sums[:, np.newaxis]
            SIS_n=np.where(np.isnan(SIS_n),0,SIS_n)
            #beta = 1.6
            #gamma = 0.04
            #public_trans = 0.5                                 # alpha
            #R0 = beta/gamma
            beta_vec = np.full(locs_len, beta)
            gamma_vec = np.full(locs_len, gamma)
            #public_trans_vec = np.full(locs_len, public_trans)
            
            # make copy of the SIS matrices 
            SIS_sim = SIS.copy()
            SIS_nsim = SIS_n.copy()
            #print(SIS_nsim)
            # run model
            #print(SIS_sim.sum(axis=0).sum() == N_k.sum())
            #from tqdm import tqdm_notebook
            infected_pop_norm = []
            susceptible_pop_norm = []
            S = SIS_sim[:,0].sum()/N_k.sum()
            I = SIS_sim[:,1].sum()/N_k.sum()
            
            infected_pop_norm.append(I)
            susceptible_pop_norm.append(S)
            
            
            for i in range(0,days):
                infected_mat = np.array([SIS_nsim[:,1],]*locs_len).transpose()
                
                OD_infected = np.round(OD*infected_mat)
                #print("OD_INF",OD_infected)
                inflow_infected = OD_infected.sum(axis=0)
                #inflow_infected = np.round(inflow_infected*public_trans_vec)
                self.k=(N_k + OD.sum(axis=0))+ (beta_vec * SIS_sim[:, 0] * SIS_sim[:, 1] / N_k)
                new_infect = beta_vec*SIS_sim[:, 0]*inflow_infected/self.k
                new_infect=np.where(np.isnan(new_infect),0,new_infect)
                new_recovered = gamma_vec*SIS_sim[:, 1]
                new_recovered=np.where(np.isnan(new_recovered),0,new_recovered)
                new_infect = np.where(new_infect>SIS_sim[:, 0], SIS_sim[:, 0], new_infect)
                
                SIS_sim[:, 0] = SIS_sim[:, 0] - new_infect + new_recovered
                SIS_sim[:, 1] = SIS_sim[:, 1] + new_infect - new_recovered
                
                SIS_sim = np.where(SIS_sim<0,0,SIS_sim)
                # recompute the normalized SIS matrix
                row_sums = SIS_sim.sum(axis=1)
                self.h=row_sums[:, np.newaxis]
                SIS_nsim = SIS_sim / self.h
                #print("siS_n")
                SIS_nsim=np.where(np.isnan(SIS_nsim),0,SIS_nsim)
                
                #print(SIS_nsim)
                S = SIS_sim[:,0].sum()/N_k.sum()
                I = SIS_sim[:,1].sum()/N_k.sum()
                
        
                #print(S, I)
                #print('\n')
                infected_pop_norm.append(I)
                susceptible_pop_norm.append(S)
            return self,infected_pop_norm,susceptible_pop_norm
