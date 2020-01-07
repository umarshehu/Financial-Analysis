# -*- coding: utf-8 -*-


import numpy as sp
cashflows=[55,-50,-50,-50,100]
n=1000
n_cashflow=len(cashflows)
epsilon=sp.abs(sp.mean(cashflows))*0.01
irr=[-99.00]
lag_sign=sp.sign(sp.npv(0,cashflows))
i=1
j=1
while(i<=n):
    interest=i*0.001
    s=sp.sign(sp.npv(interest,cashflows))
    i=i+1
    if s*lag_sign<0:
        lag_sign=s
        if j==1:
            irr=[interest]
            j=2
        else:
            irr.append(interest)
            
            
            
   
        