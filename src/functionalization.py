import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def create_subset(df, col_to_split, conditions, name_dfs_out):
    '''
    
        Takes in a dataframe, a column, and conditions on which to split the dataframe.  
        Returns two new dataframes split on the conditions provided.

            Parameters:
                    df (dataframe): Pandas dataframe
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string
    
    
    '''

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

def overlay_histograms(ax, arrays, labels, colors, title, bin_size = 30, alpha = 0.3, density = True):
    '''
        Overlays one or more histograms on same axes object.

            Parameters:
                    ax: axes object (matplotlib.pyplot)
                    *note: arrays, colors, and labels will be parallel lists
                        arrays (array of arrays): one or more arrays for the x values of each histogram
                        colors (array of strings): colors for each histogram
                        labels (array of strings): labels for each histogram
                    title (string): title for figure 
                    bin_size (int): default is 30
                    alpha (float): set transparency of plots, default is 0.3    
                    density (bool): normalize for different array lengths, default is True
            Returns:
                    Overlayed histograms on same axes object
    '''
    for arr, lab, col in zip(arrays, labels, colors):
        ax.hist(arr, label = lab, color = col, bins = bin_size, alpha = alpha)
    
    ax.set_title(title)
    ax.legend();
    return None


def log_likelihood_poisson(data, lam):
    '''
        Calculates the log likelihood for data, assuming a poisson distribution of a specified lambda.

            Parameters:
                    data (array or series): dataframe column or series
                    lam (int): rate for poisson distribution
                    
            Returns:
                    The log likelihood of a poisson distribution with lambda = lam producing the data
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
        