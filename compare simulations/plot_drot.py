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
D2 = Newman(p_exper) 

point1 = TiradoGarcia(20)
point2 = Newman(20) 

plt.plot(p_exper, D1, label = "Tirado Garcia")
plt.plot(p_exper, D2, label = "Newman")
plt.plot(20,point1,'-ro', label = "TiradoGarcia")
plt.plot(20,point2, '-go', label = "Newman")
plt.xlabel(r'$p$')
plt.ylabel(r'$D_{rot}\,(\mu m^{2} s^{-1})$')
plt.legend(title=r'$\,(nm)$')
plt.title("D_rot vs. p")
plt.savefig('plots/plot_Drot.pdf', format="pdf", bbox_inches="tight")
