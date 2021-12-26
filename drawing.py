import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from mpl_toolkits.mplot3d import axes3d

class Draw:
    fig = None;
    def __init__(self,data_name):
        df = pd.read_csv('./'+data_name)
        self.csv_data = df;
        self.fig  = plt.figure(figsize=(16,9))
    def get_police(self):
        self.police = self.csv_data["Police"]
        return self.police
    def get_citizen(self):
        self.citizen = self.csv_data["Citizen"]
        return self.citizen
    def get_doctor(self):
        self.doctor = self.csv_data["Doctor"]
        return self.doctor
    def get_mafia(self):
        self.mafia = self.csv_data["Mafia"]
        return self.mafia
    def get_mafia_win(self):
        self.mafia_rate = self.csv_data["Mafia Win Rate"]
        return self.mafia_rate
    def get_mafia_ratio(self):
        self.mafia_ratio = self.csv_data['Mafia/Citizen']
        return self.mafia_ratio
    
    def make2d(self,data_name1,data_name2,color):
        self.z = np.polyfit(self.csv_data[data_name1],self.csv_data[data_name2],1)
        self.p= np.poly1d(self.z)
        self.csv_data.plot(kind='scatter',
                 x=data_name1,
                 y=data_name2,
                marker='o',
                color=color,
                )
        self.pl = plt.plot(self.csv_data[data_name1],self.p(self.csv_data[data_name1]),"r--")
        plt.ylim(0,1.1)
        plt.show()
    def make3d(self,d1,d2,d3):
        self.fig = plt.figure(figsize = (16, 9))
        self.ax = plt.axes(projection ="3d")
        self.ax.set_zlabel('Mafia')
        self.ax.set_ylabel('Doctor')
        self.ax.set_xlabel('Citizen')    
        sctt = self.ax.scatter3D(d1, d2, d3, c = self.csv_data["Mafia Win Rate"], cmap = 'bwr')
        plt.title("doctor_mafia")
        plt.colorbar(sctt, ax = self.ax, shrink = 0.5)
        plt.show()
a = Draw('simplemafia.csv')
a_x = a.get_mafia_ratio()
a_y = a.get_mafia_win()
a_x_1 = a.get_citizen()
a_y_1 = a.get_mafia()
# a.make2d("Mafia/Citizen","Mafia Win Rate","blue")
# a.make3d(a.get_citizen(),a.get_doctor(),a.get_mafia())
b = Draw('police_mafia.csv')
b_x = b.get_mafia_ratio()
b_y = b.get_mafia_win()
c = Draw('doctor_police_mafia.csv')
c_x = c.get_mafia_ratio()
c_y = c.get_mafia_win()
plt.scatter(a_x,a_y)
plt.scatter(c_x,c_y)
plt.scatter(b_x,b_y)
z1 = np.polyfit(a_x,a_y,1)
p1= np.poly1d(z1)
pl1 = plt.plot(a_x,p1(a_x),"r--")
z2 = np.polyfit(c_x,c_y,1)
p2= np.poly1d(z2)
pl2 = plt.plot(c_x,p2(c_x),"r--")
z3 = np.polyfit(b_x,b_y,1)
p3= np.poly1d(z3)
pl3 = plt.plot(b_x,p3(b_x),"r--")
plt.legend(['simple','police&doctor','police'])
plt.show()