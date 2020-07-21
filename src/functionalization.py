import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats



def overlay_histograms(ax, arrays, labels, colors, xlabel, title, bin_size = 30, alpha = 0.3, density = True):
    '''
        Overlays one or more histograms on same axes object.

            Parameters:
                    ax: axes object (matplotlib.pyplot)
                    *note: arrays, colors, and labels will be parallel lists
                        arrays (list of arrays): one or more arrays for the x values of each histogram
                        colors (list of strings): colors for each histogram
                        labels (list of strings): labels for each histogram
                    xlabel (string): label for x-axis
                    title (string): title for figure 
                    bin_size (int): default is 30
                    alpha (float): set transparency of plots, default is 0.3    
                    density (bool): normalize for different array lengths, default is True
            Returns:
                    Overlayed histograms on same axes object
    '''
    for arr, lab, col in zip(arrays, labels, colors):
        ax.hist(arr, label = lab, color = col, bins = bin_size, alpha = alpha, density = density)
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.legend()
    return None


def plot_empirical_data(ax, df, column, label = None, color = 'blue'):
    '''
        Plots the cumulative distribution of a sample. 

            Parameters:
                    ax: axes object (matplotlib.pyplot)
                    df (pandas dataframe)
                    column (series): column within dataframe that contains the data
                    label (string): label for plot
            Returns:
                    A line plot of the sample's cumulative distribution.
    '''    
    
    x = np.arange(df[column].min(), df[column].max()+1)
    y = ([df[df[column]<=xx][column].sum() for xx in x])/(df[column]).sum()
    data = np.hstack([x,y]).reshape(-1, len(x))
    ax.plot(data[0], data[1], label = label, color = color)

def overlay_plots(ax, dfs, columns, labels, colors, title):
    '''
        Overlays two or more cumulative distribution plots on same axes object.

            Parameters:
                    ax: axes object (matplotlib.pyplot)
                    *note: arrays, colors, and labels should be parallel lists
                        dfs (list of dataframes): where data to be plotted lives
                        columns (list of column names): data from each df to plot
                        colors (array of strings): colors for each plot
                        labels (array of strings): labels for each plot
                    title (string): title for figure   
            Returns:
                    Overlayed cumulative distribution plots on same axes.
    '''
    for df, col, lab, c in zip(dfs, columns, labels, colors):
        plot_empirical_data(ax, df, col, label = lab, color = c)
    ax.set_title(title)
    ax.legend
    plt.show()

#Statistical Testing, Two Sample T-Test (independent samples)

def perform_two_samp_ttest(arr1, arr2, alpha = 0.05, equal_var = False):
    '''
        Performs a two-sample t-test for two independent samples.  
        If equal_var = False, it becomes a Welche's test assuming unequal variance.

            Parameters:
                    arr1 (array): sample 1
                    arr2 (array): sample 2
                    alpha (float): significance level (probability of making Type 1 error), default = 0.05
                    equal_var (bool): assume equal variance?
                        if False: performs Welche's t-test (assuming unequal variance)
            Returns:
                    A p-value and whether or not Null should be rejected based on significance level
    '''
    p = stats.ttest_ind(arr1, arr2, equal_var= equal_var)[1]
    if p < alpha:
        return (f"p-value = {p}: Reject the Null Hypothesis")
    else: 
        return (f"p-value = {p} Fail to Reject the Null Hypothesis") 

#MLE For Poisson Distribution
def log_likelihood_poisson(data, lam):
    '''
        Calculates the log likelihood for data, assuming a poisson distribution of a specified lambda.

            Parameters:
                    data (array or series): dataframe column or series
                    lam (int): rate for poisson distribution
                    
            Returns:
                    The log-likelihood of a poisson distribution with lambda = lam producing the data
    '''
    log_lik = -len(data) * lam
    for datum in data:
        log_lik -= math.log(math.factorial(datum)) - (np.log(lam)) * datum
    return log_lik

def mle_poisson(data, lams):
    log_liks = []
    y = np.array(data).astype(int)
    for lam in lams:
        log_liks.append(log_likelihood_poisson(y, lam))
    idx = np.argmax(log_liks)
    return lams[idx]

def bootstrap_sampling(array, num_samples, statistic):
    
    '''
        Takes in an array and creates a number of bootstrap samples (num_samples), with replacement, all of length len(array). 
        Returns an array of the bootstrap samples.

            Parameters:
                    array (array): list or series
                    num_samples (int): number of boostrap samples
                    statistic (str): aggregate statistic (i.e. np.mean) to perform on each bootstrap sample

            Returns:
                    array (array): bootstrap samples
    '''
    bootstraps = []

    for n in range(num_samples):
        samp = np.random.choice(array, len(array), replace = True)
        bootstraps.append(statistic(samp))
        
    return bootstraps