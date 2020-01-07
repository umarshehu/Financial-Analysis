# -*- coding: utf-8 -*-


def myPV(r,n,fv):
    import scipy as sp
    return(-sp.pv(r,n,0,fv))
    
    
    
def myPV(r,n,fv):
    """
    Objective: estimate present value of one future cash flow
           r : period rate
           n : number of periods
          fv: fture value
           
    formula used : pv=fv/(1+r)**n      
               
    Example 1: >>>myPV(0.1,1,100)
                 90.9090909090909
    
    Example #2 >>>myPV(r=0.1,fv=100,n=1)
                 90.9090909090909
    """
    import scipy as sp
    return(-sp.pv(r,n,0,fv))