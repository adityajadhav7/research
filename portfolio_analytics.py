import yfinance as yf
import numpy as np


tickers = ['^NSEI', '^GSPC', 'GC=F']

# Gold provides diversification in a portfolio and is often correlated with the stock market during risk-on periods - look at correlation matrix
# GC=F = Gold 
# ^GSPC = S&P 500
# ^NSEI = NIFTY 50

data = yf.downloads(tickers, start='1998-01-01')['Adj Close']
return_data = np.log(data/data.shift(1))

# Logarithmic returns are useful because they are additive. The logarithmic return of a portfolio composed of multiple assets is simply the sum of 
# the logarithmic returns of each individual asset. This makes it easy to calculate the overall performance of a portfolio over a period of time.

return_data.corr()
return_data.cumsum().plot()

return_data.mean()
return_data.std()
# An equal-weighted portfolio
W = np.ones(len(return_data.columns))/(np.ones(len(return_data.columns))).sum()

# return of portfolio
# (W * return_data.mean()).sum()
return_data.mean().dot(W)

# portfolio risk - standard deviation
# variance covariance matrix
return_data.cov()
(W.T.dot(return_data.cov().dot(W)))**(1/2)

# sharp ratio

return_data.mean()/return_data.std()

return_data.mean().dot(W)/ (W.T.dot(return_data.cov().dot(W)))**(1/2)

# reference: https://faculty.washington.edu/ezivot/econ424/portfolioTheoryMatrix.pdf

# https://www.cmegroup.com/education/files/jpm-systematic-strategies-2013-12-11-1277971.pdf
# https://www.cmegroup.com/education/files/jpm-momentum-strategies-2015-04-15-1681565.pdf
# https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4687408
