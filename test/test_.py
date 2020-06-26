from mockito import mock, verify
import unittest
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
#import pyreadr
import pandas as pd

from src.SIR_CODE import sir_c
from src.SIER_CODE import sier_c
from src.SIS_CODE import sis_c




class Testset(unittest.TestCase):
    def expectNotEmpty(self, first, second, msg=None):
        with self.subTest():
            self.assertNotEqual(first, second, msg)
    def SIR_class_objects(self):
        return sir_c(self.first_infections,self.N_k,self.OD,self.days)


    def test_SIR_RESULTS_not_empty(self):
        self.days = 200
        df = pd.read_csv("japanpop1.csv")
        # print(df)
        N = list(df['pop'])
        # print(sum(N))
        self.N_k = np.array(N)
        OD1 = pd.read_csv("od_alltrip.csv")
        self.OD = np.array(OD1)
        df3 = pd.read_csv("first_infections.csv")
        first_infection = list(df3['x'])
        self.first_infections = np.array(first_infection)
        self.recovered_pop_norm = []
        self.susceptible_pop_norm = []
        self.infected_pop_norm = []
        obj,self.infected_pop_norm, self.susceptible_pop_norm, self.recovered_pop_norm = sir_c.abc(self,self.first_infections,self.N_k,self.OD,self.days)
        #print(self.infected_pop_norm)
        #i=[]
        #s=[]
        #r=[]
        l1= len(self.infected_pop_norm)
        self.expectNotEmpty(l1, 0, "infected_error")
        l2 = len(self.susceptible_pop_norm)
        self.expectNotEmpty(l2, 0, "susceptible_error")
        l3 = len(self.susceptible_pop_norm)
        self.expectNotEmpty(l3, 0, "recovered_error")

    def test_SIR_divide_by_zero_errors(self):
        self.days = 200
        df = pd.read_csv("japanpop1.csv")
        # print(df)
        N = list(df['pop'])
        # print(sum(N))
        self.N_k = np.array(N)
        OD1 = pd.read_csv("od_alltrip.csv")
        self.OD = np.array(OD1)
        df3 = pd.read_csv("first_infections.csv")
        first_infection = list(df3['x'])
        self.first_infections = np.array(first_infection)
        self.recovered_pop_norm = []
        self.susceptible_pop_norm = []
        self.infected_pop_norm = []
        obj,self.infected_pop_norm, self.susceptible_pop_norm, self.recovered_pop_norm=sir_c.abc(self,self.first_infections,self.N_k,self.OD,self.days)
        #x=t.sir_c.__init__(self,self.first_infections,self.N_k,self.OD,self.days)
        x=np.any(obj.k!=0)
        y=np.any(obj.p!=0)
        z=np.any(obj.t!=0)
        w=np.any(self.N_k!=0)
        self.expectNotEmpty(w,False)
        self.expectNotEmpty(x,False)
        self.expectNotEmpty(y,False)
        self.expectNotEmpty(z,False)

    def test_SEIR_divide_by_zero_errors(self):
        self.days = 200
        df = pd.read_csv("japanpop1.csv")
        N = list(df['pop'])
        # print(sum(N))
        self.N_k = np.array(N)
        OD1 = pd.read_csv("od_alltrip.csv")
        self.OD = np.array(OD1)
        df3 = pd.read_csv("first_infections.csv")
        first_infection = list(df3['x'])
        self.first_infections = np.array(first_infection)
        self.recovered_pop_norm = []
        self.exp_pop_norm = []
        self.susceptible_pop_norm = []
        self.infected_pop_norm = []
        obj, self.infected_pop_norm, self.susceptible_pop_norm, self.exp_pop_norm,self.recovered_pop_norm = sier_c.abc(self,self.N_k,self.first_infections,self.days,self.OD)
        x = np.any(obj.t != 0)
        y = np.any(obj.k != 0)
        z = np.any(obj.m != 0)
        w = np.any(self.N_k != 0)
        self.expectNotEmpty(w, False)
        self.expectNotEmpty(x, False)
        self.expectNotEmpty(y, False)
        self.expectNotEmpty(z, False)

    def test_SEIR_RESULTS_NOT_EMPTY(self):
        self.days = 200
        df = pd.read_csv("japanpop1.csv")
        N = list(df['pop'])
        # print(sum(N))
        self.N_k = np.array(N)
        OD1 = pd.read_csv("od_alltrip.csv")
        self.OD = np.array(OD1)
        df3 = pd.read_csv("first_infections.csv")
        first_infection = list(df3['x'])
        self.first_infections = np.array(first_infection)
        self.recovered_pop_norm = []
        self.exp_pop_norm = []
        self.susceptible_pop_norm = []
        self.infected_pop_norm = []
        obj, self.infected_pop_norm, self.susceptible_pop_norm, self.exp_pop_norm, self.recovered_pop_norm = sier_c.abc(self, self.N_k, self.first_infections, self.days, self.OD)
        l1 = len(self.infected_pop_norm)
        self.expectNotEmpty(l1, 0, "infected_error")
        l2 = len(self.susceptible_pop_norm)
        self.expectNotEmpty(l2, 0, "susceptible_error")
        l3 = len(self.susceptible_pop_norm)
        self.expectNotEmpty(l3, 0, "recovered_error")
        l4=len(self.exp_pop_norm)
        self.expectNotEmpty(l4, 0, "recovered_error")

    def test_SIS_RESULTS_NOT_EMPTY(self):
        self.days = 70
        contact_rate = 20  # number of contacts per day
        transmission_probability = 0.3  # transmission probability
        infectious_period = 14
        beta = contact_rate * transmission_probability
        gamma = 1 / infectious_period
        df = pd.read_csv("japanpop1.csv")
        N = list(df['pop'])
        # print(sum(N))
        self.N_k = np.array(N)
        OD1 = pd.read_csv("od_alltrip.csv")
        self.OD = np.array(OD1)
        df3 = pd.read_csv("first_infections.csv")
        first_infection = list(df3['x'])
        self.first_infections = np.array(first_infection)
        self.recovered_pop_norm = []
        self.exp_pop_norm = []
        self.susceptible_pop_norm = []
        self.infected_pop_norm = []

        # Ro = beta / gamma
        # dS = (-beta * S * I) + (gamma * I)
        # dI = ( beta * S * I) - (gamma * I)
        obj,self.infected_pop_norm, self.susceptible_pop_norm = sis_c.abc(self, self.N_k, self.first_infections, self.days, self.OD, beta,
                                                                       gamma, transmission_probability, contact_rate)
        l1 = len(self.infected_pop_norm)
        self.expectNotEmpty(l1, 0, "infected_error")
        l2 = len(self.susceptible_pop_norm)
        self.expectNotEmpty(l2, 0, "susceptible_error")



    def test_SIS_divide_by_zero_errors(self):
        self.days = 70
        contact_rate = 20  # number of contacts per day
        transmission_probability = 0.3  # transmission probability
        infectious_period = 14
        beta = contact_rate * transmission_probability
        gamma = 1 / infectious_period
        df = pd.read_csv("japanpop1.csv")
        N = list(df['pop'])
        # print(sum(N))
        self.N_k = np.array(N)
        OD1 = pd.read_csv("od_alltrip.csv")
        self.OD = np.array(OD1)
        df3 = pd.read_csv("first_infections.csv")
        first_infection = list(df3['x'])
        self.first_infections = np.array(first_infection)
        self.recovered_pop_norm = []
        self.exp_pop_norm = []
        self.susceptible_pop_norm = []
        self.infected_pop_norm = []

        # Ro = beta / gamma
        # dS = (-beta * S * I) + (gamma * I)
        # dI = ( beta * S * I) - (gamma * I)
        obj,self.infected_pop_norm, self.susceptible_pop_norm = sis_c.abc(self, self.N_k, self.first_infections, self.days,
                                                                      self.OD, beta,
                                                                      gamma, transmission_probability, contact_rate)
        x = np.any(obj.t != 0)
        y = np.any(obj.k != 0)
        z = np.any(obj.h != 0)
        w = np.any(self.N_k != 0)
        self.expectNotEmpty(w, False)
        self.expectNotEmpty(x, False)
        self.expectNotEmpty(y, False)
        self.expectNotEmpty(z, False)


    if __name__ == '__main__':
        unittest.main()

    
