# -*- coding: utf-8 -*-
from math import *

# (1.)*(2)=(2.)-float * int= float
# (1.)*(2.)=(2.)-float * float= float
# Pyton 2.x
# x=1.*input("Lietotāj, lūdzu ievadi argumentu (x): ")
# Pyton 2.x
# x=float(raw_input("Lietotāj,lūdzu,ievadi argumentu (x): "))
# Pyton 3.x
x=float(input("Lietotāj,lūdzu ievādi argumentu (x): "))

y=sin(x)

print("sin(%.2f) =%2f"%(x,y))

a0=(-1)**1*0**1/(1)
S0=a0
print("a0=%.2f SO=%.2f"%(a0,S0))

a1=(-1)**1*x**3/(1*2*3)
S1=a0+a1
print("a1=%.2f S1=%.2f"%(a1,S1))

a2=(-1)**2*x**5/(1*2*3*4*5)
S2=a0+a1+a2
print("a2=%.2f S2=%.2f"%(a2,S2))

a3=(-1)**3*x**7/(1*2*3*4*5*6*7)
S3=a0+a1+a2
print("a3=%.2f S3=%.2f"%(a3,S3))




