import math 
import numpy as np 
import matplotlib.pyplot as plt

kB = 1.38E-23
T = 310
eta = 0.6913E-3
d = 2.5e-9
p_exper = np.linspace(4.6,30,300)
#this range comes from the paper 

def TiradoGarcia(p):
    v_perp = 0.839 + (0.185/p) + (0.233/(p**2))
    l = p*2*(d)
    D_perp = ((np.log(p) + v_perp)*kB*T)/(4*math.pi*eta*l)
    return D_perp

def Newman(p):
    v_perp = 0.866 -(0.15/(np.log(2*p))) - (8.1/(np.log(2*p)**2)) + (18/(np.log(2*p)**3)) - (9/(np.log(2*p)**4))
    l = p*2*(d)
    D_perp = ((np.log(p) + v_perp)*kB*T)/(4*math.pi*eta*l)
    return D_perp

D1 = TiradoGarcia(p_exper) 
D2 = Newman(p_exper) 

point1 = TiradoGarcia(20)
point2 = Newman(20) 


plt.plot(p_exper, D1, label = "Tirado Garcia")
plt.plot(p_exper, D2, label = "Newman")
plt.plot(20,point1,'-ro', label=r'$20 = {}$'.format(point1))
plt.plot(20,point2, '-go', label=r'$20 = {}$'.format(point2))
plt.xlabel(r'$p$')
plt.ylabel(r'$D_{perpendicular}\,(\mu m^{2} s^{-1})$')
plt.legend(title=r'$\,(nm)$')
plt.title("D_perp vs. p")
plt.savefig('plots/plot_Dperp.pdf', format="pdf", bbox_inches="tight")


