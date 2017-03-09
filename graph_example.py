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
    return mean_price, mean_return, stdv

def calculate_moving_average(returns, num_of_terms):
    moving_average = []
    for i in range(num_of_terms, len(returns)):
        mean = 0.0
        for j in range(num_of_terms):
            mean += returns[i - j]
        mean = mean / num_of_terms
        moving_average.append(mean)
    return moving_average

def calculate_means(data, num_of_samples, overlap):
    means = [] 
    for i in range(0, len(data), overlap):
        mean = 0.0
        count_start = i
        count_end = i
        for j in range(num_of_samples):
            if (i + j < len(data)):
                mean = mean + data[i + j]
                count_end = count_end + 1
        mean = mean / (count_end - count_start)
        means.append([mean, count_start, count_end])
    return means

def main():
    df = pd.read_csv('moh.csv')
    close_price = df['Close']
    returns, delayed_returns = calculate_returns(close_price, 365)
    x, y, stdv = calculate_statistics(close_price, returns)
    means = calculate_means(close_price, 100, 50)
    moving_average = calculate_moving_average(returns, 35)
    num_bins = 85
    x = np.arange(-10, 10, 0.001)

    f, axarr = plt.subplots(2, 3)
    axarr[0, 0].plot(df['Close'])
    for i in range(len(means)):
        axarr[0, 0].plot([means[i][1], means[i][2]], [means[i][0], means[i][0]])
    axarr[0, 0].set_title('Close Price')
    axarr[0, 1].plot(moving_average)
    axarr[0, 1].set_title('Second mean')
    axarr[1, 0].plot(returns)
    axarr[1, 0].set_title('Returns')
    axarr[1, 2].plot(delayed_returns)
    axarr[1, 2].set_title('Delayed Returns')
    axarr[1, 1].plot(x, norm.pdf(x, loc=0, scale=stdv))
    axarr[1, 1].hist(returns, num_bins,normed=True, alpha=0.5)
    axarr[1, 1].set_title('Normal distr')
    for i in range(len(means)):
        axarr[0, 2].plot([means[i][1], means[i][2]], [means[i][0], means[i][0]])
        
    axarr[0, 2].set_title('Means')
    # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
#    plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
#    plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

    plt.show()
if __name__ == "__main__":
    main()
