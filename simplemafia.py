from random import random, randrange
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
class simplemafia:
    data = []
    mafia =[]
    ncitizen = []
    percentOfmafia=0
    def __init__(self,mafia_input,ncitizen_input):
        self.mafia = [1 for x in range(mafia_input)]
        self.ncitizen = [1 for x in range(ncitizen_input)]
        self.print_m =mafia_input
        self.print_c =ncitizen_input
        self.percentOfmafia = (mafia_input/ncitizen_input)*100
        self.analyze_data=0

    def start(self):
        while len(self.mafia)!=0 or len(self.ncitizen)!=0 or len(self.mafia)>=len(self.ncitizen):
            self.all = self.mafia+self.ncitizen
            pick =randrange(0,len(self.all))
            #afternoon kill
            if pick >= len(self.mafia):
                pick -= len(self.mafia)
                self.ncitizen.pop(pick)
            else:
                self.mafia.pop(pick)
                
            if len(self.mafia)==0 or len(self.ncitizen)==0 or len(self.ncitizen)<=len(self.mafia):
                if(len(self.mafia)==0):
                    self.data.append(0)
                elif (len(self.ncitizen)==0):
                    self.data.append(1)#mafia win
                else:
                    self.data.append(1)
                break
            ##night kill
            self.ncitizen.pop(randrange(0,len(self.ncitizen)))
            if len(self.mafia)==0 or len(self.ncitizen)==0 or len(self.ncitizen)<=len(self.mafia):
                if(len(self.mafia)==0):
                    self.data.append(0)
                elif (len(self.ncitizen)==0):
                    self.data.append(1)#mafia win
                else:
                    self.data.append(1)
                break
            
    def analyze(self):
        self.analyze_data = self.data.count(1)/len(self.data)##percent of mafia win##마피아 이길경우의 확률을 저장하는 집합소
        return self.analyze_data
    
    def clear_data(self):
        self.data.clear()
        self.mafia.clear()
        self.ncitizen.clear()
        
    def print_mean(self):
        print("""MAFIA: {} , CITIZNE : {} 
              MAFIA WIN RATE:{}\n""".format(self.print_m,self.print_c, np.mean((self.all_analyze))))

    
raw_data = {"Mafia":[],"Citizen":[],"Mafia Win Rate":[],"Mafia/Citizen":[]}

for mafia in range(1,8):
    for citizen in range(mafia+1,20):
        for _ in range(10000):
            a = simplemafia(mafia,citizen)
            a.start()
        raw_data["Mafia"].append(mafia)
        raw_data["Citizen"].append(citizen)
        raw_data["Mafia Win Rate"].append(a.analyze())
        raw_data["Mafia/Citizen"].append(a.percentOfmafia)
        a.clear_data()

data = pd.DataFrame(raw_data)
data.sort_values("Mafia/Citizen")
data.to_csv("simplemafia.csv",float_format='%.7f')
        
