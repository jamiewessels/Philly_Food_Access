import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from functionalization import *

#Note: information on functions used can be found in functionalization.py

####Import Data, Split by Poverty Classification####
raw = pd.read_csv('../data/food_retail_cleaned.csv')
high_pov, not_high_pov = raw[raw['high_poverty']=='Yes'], raw[raw['high_poverty']=='No']

#####VISUALIZATIONS: Percent HPSS by Poverty Classification (Histograms and CDFs)#####
fig, ax = plt.subplots(2, figsize = (8, 15))

data = [high_pov['pct_hpss'], not_high_pov['pct_hpss']]
labels = ['High Poverty', 'Not High Poverty']
colors = ['red', 'blue']

overlay_histograms(ax[0], data, labels, colors, xlabel = 'Percent HPSS', title = 'Percent HPSS by Poverty Classification')
ax[0].set_ylabel('Density')

dfs_c = [high_pov, not_high_pov]
columns_c = ['pct_hpss', 'pct_hpss']
labels_c = ['High Poverty', 'Not High Poverty']

overlay_plots(ax[1], dfs_c, columns_c, labels_c, colors, 'CDF: Percent HPSS by Poverty Classification')
ax[1].set_xlabel('Percent HPSS')
ax[1].set_ylabel('Cumulative Density')

# fig.savefig('../images/pdfandcdf_pct_HPSS_by_poverty.jpeg', pad_inches = 0)
# plt.show()


#####HYPOTHESIS TESTING: Median Percent HPSS by Poverty Classification#####

fig, ax = plt.subplots(figsize = (10, 10))
num_bs_samps = 5000
conf_level = 0.95
plot_bs_sample_diffs(ax, high_pov['pct_hpss'], not_high_pov['pct_hpss'], num_bs_samps, np.median, conf_level, 'Comparison of Median %HPSS based on Poverty Classification', 'Difference in Bootstrap Sample Medians: \n Sample1: High Poverty Areas (> 20%) | Sample 2: Not High Poverty Areas (< 20%)')
fig.tight_layout()
# fig.savefig('../images/Percent_HPSS_compare_medians.jpeg')
# plt.show()
