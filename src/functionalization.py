import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def overlay_histograms(ax, arrays, labels, colors, xlabel, title, bin_size = 30, alpha = 0.3, density = True):
    '''
        Overlays one or more histograms on same axes object.

            Parameters:
                    ax: axes object (matplotlib.pyplot)
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
    
    ax.set_title(title, fontsize = 15)
    ax.set_xlabel(xlabel, fontsize = 12)
    ax.legend(fontsize = 12)


def plot_empirical_data(ax, df, column, label = None, color = 'blue'):
    '''
        Plots the approximate cumulative distribution of a sample. 

            Parameters:
                    ax: axes object (matplotlib.pyplot)
                    df (pandas dataframe)
                    column (string): column name within dataframe that contains the data
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
                    dfs (list of strings): strings are the dataframe names
                    columns (list of strings): strings are the column names from each dataframe
                    colors (array of strings): colors for each plot
                    labels (array of strings): labels for each plot
                    title (string): title for figure   
            Returns:
                    Overlayed cumulative distribution plots on same axes.
    '''
    for df, col, lab, c in zip(dfs, columns, labels, colors):
        plot_empirical_data(ax, df, col, label = lab, color = c)
    ax.set_title(title, fontsize = 15)
    ax.legend(fontsize = 12)
    # plt.show()


def paired_bootstrap_sampling(sample1, sample2, num_samples, statistic):
    
    '''
        Takes in two arrays and creates a number (=num_samples) of bootstrap samples.
        Each bootstrap sample is aggregated on the statistic parameter.
        The differences of each sample's aggregates are calculated and added to the output list.

            Parameters:
                    sample1 (array): first sample for comparison
                    sample1 (array): second sample for comparison
                    num_samples (int): number of boostrap samples
                    statistic (str): aggregate statistic (i.e. np.median) to perform on each bootstrap sample

            Returns:
                    array (array): differences in statistic for each boostrap samples, length = num_samples
    '''
    bootstraps = []

    for n in range(num_samples):
        samp1 = np.random.choice(sample1, len(sample1), replace = True)
        samp2 = np.random.choice(sample2, len(sample2), replace = True)
        bootstraps.append(statistic(samp1) - statistic(samp2))
        
    return bootstraps

def plot_bs_sample_diffs(ax, sample1, sample2, num_samples, statistic, conf, title, xlabel, alpha = 0.5):

    '''
            Plots a histogram of the output of function "paired_boostrap_sampling".
            Calculates a confidence interval based on percentiles.

            Parameters:
                    ax: axes object (matplotlib.pyplot)
                    sample1 (array): first sample for comparison
                    sample1 (array): second sample for comparison
                    num_samples (int): number of boostrap samples
                    statistic (str): aggregate statistic (i.e. np.median) to perform on each bootstrap sample
                    conf (float): confidence interval (i.e. 0.95 for 95%)
                    title (string): figure title
                    xlabel (string): x-axis label
                    alpha (float): set transparency of plots, default is 0.3    

            Returns:
                    plot of the output from function "paired_boostrap_sampling"
                    confidence intervals for the difference in the statistic between the two samples
    '''
    diffs = paired_bootstrap_sampling(sample1, sample2, num_samples, statistic)
    sorted_diffs = sorted(diffs)
    
    ci_lower_limit = sorted_diffs[int(num_samples * (1-conf)/2)]
    ci_upper_limit = sorted_diffs[int(num_samples * ((1-conf)/2 +conf))]
    print(f'lower CI: {ci_lower_limit}, upper CI: {ci_upper_limit}')
    
    ax.hist(diffs, density = True, bins = 20, alpha = alpha)
    ax.axvline(x = ci_lower_limit, linestyle = 'dashed', color = 'blue', label = f'CI Lower: {ci_lower_limit.round(3)}')
    ax.axvline(x = ci_upper_limit, linestyle = 'dashed', color = 'green', label = f'CI Upper: {ci_upper_limit.round(3)}')
    ax.set_xlabel(xlabel, fontsize = 12)
    ax.set_title(title, fontsize = 15)
    ax.set_ylabel('Density', fontsize = 12)
    ax.legend(fontsize = 12)
    

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