import matplotlib

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
#import pyreadr
import pandas as pd
class sir_c:
    def abc(self,f,N,O,days):
            N_k=N
            locs_len = len(N_k)                 # number of locations
            #print(locs_len)
            first_infections=f
            OD=O
            SIR = np.zeros(shape=(locs_len, 3)) # make a numpy array with 3 columns for keeping track of the S, I, R groups
            SIR[:,0] = N_k                      # initialize the S group with the respective populations
            #first_infections = np.where(SIR[:, 0]<=50, SIR[:, 0]//20, 0)   # for demo purposes, randomly introduce infections
            np.seterr(divide='ignore', invalid='ignore')
            SIR[:, 0] = SIR[:, 0] - first_infections
            SIR[:, 1] = SIR[:, 1] + first_infections                           # move infections to the I group
            # row normalize the SIR matrix for keeping track of group proportions
            row_sums = SIR.sum(axis=1)
            self.k=row_sums[:, np.newaxis]
            SIR_n = SIR / row_sums[:, np.newaxis]
            SIR_n=np.where(np.isnan(SIR_n),0,SIR_n)
            beta = 0.3
            gamma = 0.2
            
            #R0 = beta/gamma
            beta_vec = np.full(locs_len,beta)
            gamma_vec = np.full(locs_len, gamma)
            
            
            # make copy of the SIR matrices 
            SIR_sim = SIR.copy()
            SIR_nsim = SIR_n.copy()
            
            # run model
            print(SIR_sim.sum(axis=0).sum() == N_k.sum())
            
            S = SIR_sim[:,0].sum()/N_k.sum()
            I = SIR_sim[:,1].sum()/N_k.sum()
            R = SIR_sim[:,2].sum()/N_k.sum()
            infected_pop_norm=[I]
            susceptible_pop_norm = [S]
            recovered_pop_norm = [R]
            

            for i in range(0,days):
                infected_mat = np.repeat([SIR_nsim[:,1],],repeats=3774,axis=0)
                OD_infected = np.round(OD*infected_mat)
                #print("OD_INF",OD_infected)
                inflow_infected = OD_infected.sum(axis=0)
                self.p=(N_k + OD.sum(axis=0))+(beta_vec * SIR_sim[:, 0] * SIR_sim[:, 1] / N_k)
                new_infect = beta_vec*SIR_sim[:, 0]*inflow_infected/(N_k + OD.sum(axis=0))+(beta_vec * SIR_sim[:, 0] * SIR_sim[:, 1] / N_k)
                new_infect=np.where(np.isnan(new_infect),0,new_infect)
                
                new_recovered = gamma_vec*SIR_sim[:, 1]
                new_recovered=np.where(np.isnan(new_recovered),0,new_recovered)
                
                #new_infect = np.where(new_infect>SIR_sim[:, 0], SIR_sim[:, 0], new_infect)
                SIR_sim[:, 0] = SIR_sim[:, 0] - new_infect
                SIR_sim[:, 1] = SIR_sim[:, 1] + new_infect - new_recovered
                SIR_sim[:, 2] = SIR_sim[:, 2] + new_recovered
                SIR_sim = np.where(SIR_sim<0,0,SIR_sim)
                # recompute the normalized SIR matrix
                row_sums = SIR_sim.sum(axis=1)
                self.t=row_sums[:, np.newaxis]
                SIR_nsim = SIR_sim /row_sums[:, np.newaxis]
                SIR_nsim=np.where(np.isnan(SIR_nsim),0,SIR_n)
                
                S = SIR_sim[:,0].sum()/N_k.sum()
                I = SIR_sim[:,1].sum()/N_k.sum()
                R = SIR_sim[:,2].sum()/N_k.sum()
                infected_pop_norm.append(I)
                susceptible_pop_norm.append(S)
                recovered_pop_norm.append(R)
            return (self,infected_pop_norm,susceptible_pop_norm,recovered_pop_norm)
                
          
