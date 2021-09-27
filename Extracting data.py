import pandas as pd
import numpy as np
import os
import seaborn as sea
import matplotlib.pyplot as plt


def extract(dir = 'Caso_conT_00/extract_conT',sim_time = 40,time_step= 0.05,start_time=0.05,var='Ec'):
    list = ['extract_'+ str(v) + '.csv' for v in range(0,len(os.listdir(dir)))]
    Ec = []
    for i in list:
        df = pd.read_csv(dir + '/'+i,float_precision= 'high')
        Ec.append(df[var].iloc[0])
    ind = [round(n,2) for n in np.arange(start_time,sim_time+0.05,time_step)]
    s = pd.Series(Ec,index=ind)
    return s
def plotting(Ec,xl= 'Tiempo [s]',yl= 'Ec [m^2/s^2]',title = 'Title'):
    sea.set_theme()
    sea.set_style('ticks')
    plt.figure(figsize=(15, 7))
    sea.lineplot(data=Ec)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(label= title,fontsize= 25,fontstyle='italic',color = 'blue')
    return plt.show()

##Energía cinética
#Ec_conT = extract()
#Ec_sinT = extract(dir = 'extract_sinT')
#Ec = pd.DataFrame({'Ec con T':Ec_conT,'Ec sin T':Ec_sinT})
#plotting(Ec,title='Simulación de 40s')

#Temperatura
T_conT = extract(var='T')
#plot= sea.lineplot(data=T_conT)
plotting(T_conT,yl='Temperatura [K]',title='Simulación 40s caso 0,0')

#Presión
#P_conT = extract(var='p')
#P_sinT= extract(dir='extract_sinT',var='p')
#P = pd.DataFrame({'P con T':P_conT,'P sin T':P_sinT})
#plotting(P,yl= 'Presión cinemática [m^2/s^2]',title= 'Simulación de 40s')

#Vorticidad
#V_conT = extract(dir='Vorticidad/V con t/vorticity',var='Vort')
#V_sinT = extract(dir='Vorticidad/V sin t/vorticidad',var='Vort')
#V = pd.DataFrame({'V con T':V_conT,'V sin T':V_sinT})
#lotting(V,yl= 'Vorticidad',title= 'Simulación de 40s')