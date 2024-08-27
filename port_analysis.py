import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Create a list of tickers and weights
tickers = ['ASIANPAINT.NS', 'ASTRAL.NS', 'BAJFINANCE.NS', 'CHOLAFIN.NS', 'CMSINFO.NS','DIVISLAB.NS','LALPATHLAB.NS','ESCORTS.NS','EICHERMOT.NS',
          'HDFCBANK.NS','ICICIGI.NS','METROBRAND.NS','NH.NS','PIDILITIND.NS','TATACONSUM.NS','TITAN.NS','TRENT.NS','TIINDIA.NS']
wts = [0.0555]*18

from pandas_datareader import data as pdr
import fix_yahoo_finance as yfin
price_data = yfin.pdr_override(tickers, start = '2023-08-01',
                               end = '2024-07-31')


price_data = price_data["Adj Close"]

ret_data = price_data.pct_change()[1:]

ret_data.shape

port_ret = (ret_data * wts).sum(axis = 1)

port_ret.values



benchmark_price  = yfin.pdr_override('^NSEI', start = '2023-08-01',
                               end = '2024-07-31')
                               
benchmark_ret = benchmark_price["Adj Close"].pct_change()[1:]

sns.regplot(x=benchmark_ret.values,y=port_ret.values)
plt.xlabel("Benchmark Returns")
plt.ylabel("Portfolio Returns")
plt.title("Portfolio Returns vs Benchmark Returns")
plt.show()

(beta, alpha) = stats.linregress(benchmark_ret.values,
                port_ret.values)[0:2]
                
print("The portfolio beta is", round(beta, 4))



print("The portfolio beta is", round(alpha,5))

cov_ = np.stack((benchmark_ret.values, port_ret.values), axis=0)

covariance = np.cov(cov_)

var = np.var(benchmark_ret.values)
var

beta = covariance[0,1]/var

all_weights = np.zeros((10000,18))

ret_arr = np.zeros(10000)
vol_arr = np.zeros(10000)
sharp_arr = np.zeros(10000)
for i in range(0,10000):
    weights = np.array(np.random.random(18))
    weights = weights/weights.sum()
    all_weights[i,:] = weights
    ret_arr[i] = np.sum(ret_data.mean()*242*weights)
    vol_arr[i] = np.sqrt(np.dot(weights.T,np.dot(ret_data.cov()*242,weights)))
    sharp_arr[i] = ret_arr[i]/vol_arr[i]


plt.scatter(vol_arr,ret_arr, cmap='plasma', c=sharp_arr)

sharp_arr.max()

sharp_arr.argmax()


all_weights[6408,:]*100


# TODO: compute beta for all the weights 
# TODO: compute beta for max sharp wights
# TODO: compute beta for his portfolio guess by current performance

# TODO: compute industrywise exposure 

# ref: https://mishraayush447.medium.com/portfolio-optimization-using-python-b8d2b64e520e and https://www.codingfinance.com/post/2018-04-25-portfolio-beta-py/
# ref: https://www.youtube.com/watch?v=Zc67XB4voC4
