from random import random, randrange, uniform
import numpy as np    
import pandas as pd
from pandas.core.frame import DataFrame


class police_add_mafia():
    data = []
    mafia =[]
    ncitizen = []
    
    def __init__(self,mafia_input, citizen_input,police):
    
        self.mafia = [1 for x in range(mafia_input)]
        self.ncitizen = [1 for x in range(citizen_input)]
        self.percentOfmafia = (mafia_input/citizen_input)*100
        self.pick = randrange(0,len(self.ncitizen))
        self.ncitizen= self.police_make(self.ncitizen,self.pick,police)
        self.print_m= mafia_input
        self.print_c = citizen_input
        self.print_p = police
        self.analyze_data=0
        self.police_kill_mafia_rate = 1.2
        
    def police_make(self,list,pick,count):
        if count==0:
            return list
        if list[pick]==2:
            pick = randrange(0,len(list))
            return self.police_make(list,pick,count)
        else:
            list[pick]=2
            return self.police_make(list,pick,count-1)
        
    def start(self):
        while len(self.mafia)!=0 or len(self.ncitizen)!=0 or len(self.mafia)>=len(self.ncitizen):
            mafia_len = len(self.mafia)
            ncitizne_len = len(self.ncitizen)
            all= mafia_len+ncitizne_len
            if self.ncitizen.count(2)>=1:#police alive
                police_pick =randrange(0,all)
                if police_pick < len(self.mafia):#police find mafia
                    mafia_len= mafia_len*(1+self.police_kill_mafia_rate)
                    self.pick= uniform(0,mafia_len+ncitizne_len)
            else:
                self.pick =randrange(0,all)
            #afternoon kill
            if self.pick > mafia_len:
                self.ncitizen.pop()
            else:
                self.mafia.pop()
                
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
        self.analyze_data = self.data.count(1)/len(self.data)##percent of mafia win
        return self.analyze_data
    
    def clear_data(self):
        self.data.clear()
        self.mafia.clear()
        self.ncitizen.clear()
        
    def print_mean(self):
        print("""MAFIA: {} , CITIZNE : {} ,POLICE :{} 
              MAFIA WIN RATE:{}\n""".format(self.print_m,self.print_c,self.print_p, np.mean((self.all_analyze))))

raw_data = {"Mafia":[],"Citizen":[],"Police":[],"Mafia/Citizen":[],"Mafia Win Rate":[]}

for mafia in range(1,8):
    for citizen in range(mafia+1,20):
        for police in range(1,int(citizen/2)):
            for _ in range(10000):
                a = police_add_mafia(mafia,citizen,police)
                a.start()
            raw_data["Mafia"].append(mafia)
            raw_data["Citizen"].append(citizen)
            raw_data["Police"].append(police)
            raw_data["Mafia Win Rate"].append(a.analyze())
            raw_data["Mafia/Citizen"].append(a.percentOfmafia)
            a.clear_data()


data = pd.DataFrame(raw_data)
data.sort_values("Mafia/Citizen")
data.to_csv("police_mafia.csv",float_format='%.7f')