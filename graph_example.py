import pandas as pd
import numpy as np
from  scipy.stats import norm
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def calculate_returns(close_price, delay):
    ## Calculate Returns ##
    returns = []
    for i in range(close_price.size - 1):
        returns.append((close_price[i + 1] - close_price[i]) / close_price[i] *
                100)

    ## Calculate Delayed Returns ##
    delayed_returns = []
    for i in range(close_price.size - delay):
        delayed_returns.append((close_price[i + delay] - close_price[i]) / close_price[i] *
                100)
    return returns, delayed_returns

def calculate_statistics(close_price, returns):
    ## Calculate delayed mean##
    mean_5 = []
    for i in range(close_price.size - 5):
        mean_5.append((close_price[i+5] + close_price[i]) / 2);

    print "max return: ", max(returns)
    print "min return: ", min(returns)

    mean_price = sum(close_price) / len(close_price) 
    mean_return = sum(returns) / len(returns)
    print "mean price: ", mean_price 
    print "mean return: ", mean_return 

    var = 0
    stdv = 0
    for i in returns:
        var = var + pow((i - mean_return), 2)

    var = var / (len(returns) - 1)
    stdv = math.sqrt(var)
    print "Stdv : ", stdv
    print "Var : ", var
    return mean_5, mean_price, mean_return, stdv
    
def main():
    df = pd.read_csv('gi.csv')
    
    returns, delayed_returns = calculate_returns(df['Close'], 365)
    mean_5, x, y, stdv = calculate_statistics(df['Close'], returns)
    num_bins = 85
    x = np.arange(-10, 10, 0.001)

    f, axarr = plt.subplots(2, 3)
    axarr[0, 0].plot(df['Close'])
    axarr[0, 0].set_title('Close Price')
    axarr[0, 1].plot(mean_5)
    axarr[0, 1].set_title('Second mean')
    axarr[1, 0].plot(returns)
    axarr[1, 0].set_title('Returns')
    axarr[1, 2].plot(delayed_returns)
    axarr[1, 2].set_title('Delayed Returns')
    axarr[1, 1].plot(x, norm.pdf(x, loc=0, scale=stdv))
    axarr[1, 1].hist(returns, num_bins,normed=True, alpha=0.5)
    axarr[1, 1].set_title('Normal distr')
    # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
#    plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
#    plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

    plt.show()
if __name__ == "__main__":
    main()
