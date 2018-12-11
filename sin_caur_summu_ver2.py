# -*- coding: utf-8 -*-
from math import sin as standarta_sinuss
# a0, a1, a2, a3 ->
x=float(input("Lietotāj,lūdzu, ievadi argumentu (x): "))
y=standarta_sinuss(x)
print("sin(%.2f)=%6.2f"%(x,y))

#a0=(-1)**0*x**1/(1)
a=(-1)**0*x**1/(1)
#S=a0
S = a
print("a0=%6.2f S0=%6.2f"%(a,S))
                
#a1=(-1)**1**1/(1)
#a1=a0*(-1)*x*x*/(2*3)
a=a*(-1)*x*x/(2*3)
#S=S+a1
S=S+a
print("a1=%6.2f S1=%6.2f"%(a,S))

#a2=(-1)**2*x**5/(1*2*3*4*5)
#a2=a1*(-1)*x*x/(4*5)                
a=a*(-1)*x*x/(4*5)
#S=S+a2
S=S+a
print("a2=%6.2f S2=%6.2f"%(a,S))

#a3=(-1)**3*x**7/(1*2*3*4*5*6*7)
#a3=a2*(-1)*x*x/(6*7)
a=a*(-1)*x*x/(6*7)
#S=S+a3
S=S+a
print("a3=%6.2f S3=%6.2f"%(a,S))
                

