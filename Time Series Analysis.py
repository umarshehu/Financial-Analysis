
from scipy import stats 
from matplotlib.finance import quotes_historical_yahoo_ochl as getData 
import numpy as np 

ticker='IBM' 
begdate=(2012,1,1) 
enddate=(2016,12,31) 

p =getData(ticker, begdate, enddate,asobject=True, adjusted=True) 
ret = (p.aclose[1:] - p.aclose[:-1])/p.aclose[1:] 
print 'ticker=',ticker,'W-test, and P-value' 
print(stats.shapiro(ret))


print( stats.anderson(ret) )