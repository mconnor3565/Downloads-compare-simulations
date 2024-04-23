import math 
import numpy as np 
import matplotlib.pyplot as plt

kB = 1.38E-23
T = 310
eta = 0.6913E-3
d = 2.5e-9 

p_exper = np.linspace(4,20,1000)
#this range comes from the paper 


def TiradoGarcia(p):
    delta_perp = -0.662 + (0.917/p) - (0.050/(p**2))
    l = p*2*(d)
    D_rot = ((np.log(p) + delta_perp)*3*kB*T)/(math.pi*eta*(l**3))
    return D_rot
def Newman(p):
    delta_perp = -0.446 -(0.2/(np.log(2*p))) -(16/(np.log(2*p)**2)) + (63/(np.log(2*p)**3)) - (62/(np.log(2*p)**4))
    l = p*2*(d)
    D_rot = ((np.log(p) + delta_perp)*3*kB*T)/(math.pi*eta*(l**3))
    return D_rot

D1 = TiradoGarcia(p_exper) 
Da= D1[0]
D1 = D1/Da
D2 = Newman(p_exper) 
Db = D2[0]
D2 = D2/Db


point1 = TiradoGarcia(20)
point2 = Newman(20) 

pl = [4,6,8,10,12,14,16,18,20]
Drotl = [1, 0.363455443, 0.178742537, 0.090572713, 0.057639861,0.031326012, 0.020712022 , 0.020564605 , 0.015478735]


plt.plot(pl, Drotl, label = "LAMMPS")
plt.plot(p_exper, D1, label = "Tirado Garcia")
plt.plot(p_exper, D2, label = "Broersma")
# plt.plot(20,point1,'-ro', label=r'$20 = {}$'.format(point1))
# plt.plot(20,point2, '-go', label=r'$20 = {}$'.format(point2))
plt.xlabel(r'$p\, (length\, of\, molecule)$')
plt.ylabel(r'$D_{rot}\, / D_{rot}0  $')
plt.legend(title = r'$for\, D_{rot}0\, p = 4$')
plt.title(r'$D_{rot}\, vs. p$')
plt.savefig('plots/plot_Drot.pdf', format="pdf", bbox_inches="tight")
