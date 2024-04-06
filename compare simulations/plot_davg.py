import math 
import numpy as np 
import matplotlib.pyplot as plt

kB = 1.38E-23
T = 310
eta = 0.6913E-3
d =2.5e-9

p_exper = np.linspace(4.6,30,300)
#this range comes from the paper 

def TiradoGarcia(p):
    v_avg = 0.312 + (0.565/p) + (0.100/(p**2))
    l = p_exper*2*(d)
    D_avg = ((np.log(p) + v_avg)*kB*T)/(3*math.pi*eta*l)
    return D_avg

def Newman(p):
    v_perp = 0.866 -(0.15/(np.log(2*p))) - (8.1/(np.log(2*p)**2)) + (18/(np.log(2*p)**3)) - (9/(np.log(2*p)**4))
    v_para = -0.114 - (0.15/(np.log(2*p))) -(13.5/(np.log(2*p)**2)) + (37/(np.log(2*p)**3)) - (22/(np.log(2*p)**4))
    v_avg = (v_para + v_perp)/2
    l = p_exper*2*(d)
    D_avg = ((np.log(p) + v_avg)*kB*T)/(3*math.pi*eta*l)
    return D_avg

D1 = TiradoGarcia(p_exper) 
D2 = Newman(p_exper) 

plt.figure(tight_layout=True)
plt.plot(p_exper, D1, label = "Tirado Garcia")
plt.plot(p_exper, D2, label = "Newman")
plt.xlabel(r'$p$')
plt.ylabel(r'$D_{avg}\,(\mu m^{2} s^{-1})$')
plt.legend(title=r'$\,(nm)$')
plt.title("D_avg vs. p")
plt.savefig("plots/plot_Davg.pdf", format="pdf", bbox_inches="tight")




