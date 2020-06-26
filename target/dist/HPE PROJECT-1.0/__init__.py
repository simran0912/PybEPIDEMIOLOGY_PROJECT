import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
#import pyreadr
import pandas as pd
from SIR_CODE import sir_c
from SIER_CODE import sier_c
from SIS_CODE import sis_c
matplotlib.use('Agg')

        
class App(object):
    def __init__(self):
        self.r= Tk()
        self.f= Frame(self.r)
        self.la=Label(self.r)
        self.seir_sim=0
        self.f.pack()
        self.fc=Frame(self.f)
        self.days=0
        self.buttoncon=0
        self.infected_pop_norm=[]
        self.susceptible_pop_norm = []
        self.recovered_pop_norm = []
        self.exp_pop_norm=[]
        self.sis_sim=1
        self.r.title('Try graph') 
        self.b1 = Button(self.r, text='Start Simulation', width=25, command=self.sim)
        self.b2 = Button(self.r, text='Infected Plot', width=25, command=self.inf)
        self.b3 = Button(self.r, text='Susceptible Plot', width=25, command=self.sus)
        self.b4 = Button(self.r, text='Recovery Plot', width=25, command=self.rec)
        self.b5 = Button(self.r, text='Exposed Plot', width=25, command=self.exp)
        self.l=Listbox(self.r,width=25,height=3)
        self.l.insert(1,'SIR')
        self.l.insert(2,'SEIR')
        self.l.insert(3,'SIS')
        self.canvas=Canvas(self.fc,bg="white")
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        self.b4.pack()
        self.b5.pack()
        self.l.pack()
        self.fc.pack()
        self.r.mainloop()
    
        
    def inf(self):
        if(self.buttoncon==1):
            self.fc.destroy()
            self.fc=Frame(self.f)
            self.fc.pack()
            fig = Figure(figsize=(6,4))
            a = fig.add_subplot(111)
            
                    #a.plot(range(1,days+2),susceptible_pop_norm,color='blue')
            a.plot(range(1,self.days+2),self.infected_pop_norm,color='red')
            print(a)
            a.set_title ("Infected", fontsize=16)
            a.set_ylabel("Normalised Infected", fontsize=10)
            a.set_xlabel("Days", fontsize=10)
                    
            self.canvas = FigureCanvasTkAgg(fig, master=self.fc)
            self.canvas.get_tk_widget().pack()
            self.canvas.draw()
    
    def sus(self):
        if(self.buttoncon==1):      
            self.fc.destroy()           
            self.fc=Frame(self.f)
            self.fc.pack()
            fig = Figure(figsize=(6,4))
            a = fig.add_subplot(111)  
            a.plot(range(1,self.days+2),self.susceptible_pop_norm,color='blue')
            #a.plot(range(1,days+2),infected_pop_norm,color='red')
            a.set_title ("Susceptible", fontsize=16)
            a.set_ylabel("Normalized Susceptible", fontsize=10)
            a.set_xlabel("Days", fontsize=10)  
            self.canvas = FigureCanvasTkAgg(fig, master=self.fc)
            self.canvas.get_tk_widget().pack()
            self.canvas.draw()
        
    def rec(self):
        if(self.buttoncon==1 and self.sis_sim!=1):
         
         
            self.fc.destroy()
            
            self.fc=Frame(self.f)
            self.fc.pack()
            fig = Figure(figsize=(6,4))
            a = fig.add_subplot(111)  
            a.plot(range(1,self.days+2),self.recovered_pop_norm,color='blue')
            #a.plot(range(1,days+2),infected_pop_norm,color='red')
            a.set_title ("Recovery", fontsize=16)
            a.set_ylabel("Normalized Recovery", fontsize=10)
            a.set_xlabel("Days", fontsize=10) 
            self.canvas = FigureCanvasTkAgg(fig, master=self.fc)
            self.canvas.get_tk_widget().pack()
            self.canvas.draw()
    def exp(self):
        if(self.buttoncon==1 and self.seir_sim==1):
         
         
            self.fc.destroy()
            
            self.fc=Frame(self.f)
            self.fc.pack()
            fig = Figure(figsize=(6,4))
            a = fig.add_subplot(111)  
            a.plot(range(1,self.days+2),self.exp_pop_norm,color='blue')
            #a.plot(range(1,days+2),infected_pop_norm,color='red')
            a.set_title ("Exposed", fontsize=16)
            a.set_ylabel("Normalized exposed", fontsize=10)
            a.set_xlabel("Days", fontsize=10) 
            self.canvas = FigureCanvasTkAgg(fig, master=self.fc)
            self.canvas.get_tk_widget().pack()
            self.canvas.draw()
        
    def sim (self):
        print("came")
        self.sis_sim=1 #deactivate recovery button
        self.seir_sim=0 #deactivate exposed button
        self.buttoncon=1  #activate infected and recovery plot buttons
        self.days=200
        df=pd.read_csv("japanpop1.csv")
        #print(df)
        N=list(df['pop'])
        #print(sum(N))
        N_k=np.array(N)
        OD1=pd.read_csv("od_alltrip.csv")
        OD=np.array(OD1)
        df3=pd.read_csv("first_infections.csv")
        first_infection=list(df3['x'])
        first_infections=np.array(first_infection)
        #print((first_infections))
        #print(self.l)

        if(self.l.get(self.l.curselection())=='SIR'):
            self.sis_sim=0  #activate recovery button    
            obj,self.infected_pop_norm,self.susceptible_pop_norm,self.recovered_pop_norm=sir_c.abc(self,first_infections,N_k,OD,self.days)



        if(self.l.get(self.l.curselection())=='SEIR'):
            self.sis_sim=0  #activate recovery button
            self.seir_sim=1 #activate recovery button
            obj,self.infected_pop_norm,self.susceptible_pop_norm,self.exp_pop_norm,self.recovered_pop_norm = sier_c.abc(self,N_k,first_infections,self.days,OD)
            # initialize the population vector from the origin-destination flow matrix
            #OD=np.array([[100,12,33,56],[34,23,435,56],[34,23,4,56],[55,67,56,43]])
            #N_k = np.abs(np.diagonal(OD) + OD.sum(axis=0) - OD.sum(axis=1))
                    
        if(self.l.get(self.l.curselection())=='SIS'):
            #print("SIS")
            self.days=70
            contact_rate = 20                     # number of contacts per day
            transmission_probability = 0.3       # transmission probability
            infectious_period = 14   
            beta = contact_rate * transmission_probability
            gamma = 1 / infectious_period
            #Ro = beta / gamma
            #dS = (-beta * S * I) + (gamma * I)
            #dI = ( beta * S * I) - (gamma * I)
            obj,self.infected_pop_norm,self.susceptible_pop_norm=sis_c.abc(self,N_k,first_infections,self.days,OD,beta,gamma,transmission_probability,contact_rate)
                
                
                    
    def __del_(self):
        self.r.destroy()

if __name__ == "__main__":
    App()


