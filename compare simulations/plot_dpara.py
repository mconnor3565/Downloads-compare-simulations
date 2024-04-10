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
    v_para = -0.207 + (0.980/p) - (0.133/(p**2))
    l = p*2*(d)
    D_para = ((np.log(p) + v_para)*kB*T)/(2*math.pi*eta*l)
    return D_para

def Newman(p):
    v_para = -0.114 - (0.15/(np.log(2*p))) -(13.5/(np.log(2*p)**2)) + (37/(np.log(2*p)**3)) - (22/(np.log(2*p)**4))
    l = p*2*(d)
    D_para = ((np.log(p) + v_para)*kB*T)/(2*math.pi*eta*l)
    return D_para

D1 = TiradoGarcia(p_exper) 
D2 = Newman(p_exper) 


with open('Dpara.txt', 'w') as file:
    file.write("# p \t D_TG \t D_N \t \n")
    for i in range(len(p_exper)):
        file.write("{} \t {} \t {}\n".format( p_exper[i], D1[i], D2[i]))
    file.close()

point1 = TiradoGarcia(20)
point2 = Newman(20) 


plt.plot(p_exper, D1, label = "Tirado Garcia")
plt.plot(p_exper, D2, label = "Newman")
plt.plot(20,point1,'-ro', label = "TiradoGarcia")
plt.plot(20,point2, '-go', label = "Newman")
plt.xlabel(r'$p$')
plt.ylabel(r'$D_{\parallel}\,(\mu m^{2} s^{-1})$')
plt.legend(title=r'$\,(nm)$')
plt.title("D_para vs. p")
plt.savefig("plots/plot_Dpara.pdf", format="pdf", bbox_inches="tight")


