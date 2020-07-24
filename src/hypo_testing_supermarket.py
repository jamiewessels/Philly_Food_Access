import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from functionalization import *
plt.rcParams.update({'font.size': 16})

#Note: information on functions used can be found in functionalization.py

####Import Data, Split by Supermarket Access####
raw = pd.read_csv('../data/food_retail_cleaned.csv')
sprmkt_access, no_sprmkt_access = raw[raw['sprmkt_access']=='Yes'], raw[raw['sprmkt_access']=='No']

#####VISUALIZATIONS: Vehicle Availability by Supermarket Access (Histograms and CDFs)#####
fig, ax = plt.subplots(2, figsize = (8, 12))

data = [sprmkt_access['pct_vehicle_avail'], no_sprmkt_access['pct_vehicle_avail']]
labels = ['Supermarket within 0.5 mi', 'No Supermarket within 0.5 mi']
colors = ['blue', 'red']

overlay_histograms(ax[0], data, labels, colors, xlabel = 'Vehicle Availability (%)', title = 'Vehicle Availability by Supermarket Access')
ax[0].set_ylabel('Density')
ax[0].set_xlabel('Vehicle Availability (%)')

dfs_c = [sprmkt_access, no_sprmkt_access]
columns_c = ['pct_vehicle_avail', 'pct_vehicle_avail']
labels_c = ['Supermarket within 0.5 mi', 'No Supermarket within 0.5 mi']

overlay_plots(ax[1], dfs_c, columns_c, labels_c, colors, 'CDF: Poverty Percentage Based on Supermarket Access')
ax[1].set_xlabel('Vehicle Availability (%)')
ax[1].set_ylabel('Cumulative Density')

fig.savefig('../images/pdfandcdf_pct_vehicle_by_supermarket.jpeg')
plt.subplots_adjust(top=0.5)
fig.tight_layout(pad = 2.5)
plt.show()


#####HYPOTHESIS TESTING: Mean Vehicle Availability by Supermarket Access (PDF and CDF)#####
fig, ax = plt.subplots(figsize = (8, 8))
num_bs_samps = 5000
conf_level = 0.95
plot_bs_sample_diffs(ax, no_sprmkt_access['pct_vehicle_avail'], sprmkt_access['pct_vehicle_avail'], num_bs_samps, np.mean, conf_level, 'Comparison of Mean Vehicle Availability based on Supermarket Access', 'Difference in Bootstrap Sample Means: \n Sample1: Supermarket Access (within 0.5 mi) | Sample 2: No Supermarket Access')
ax.set_ylabel('Density')
fig.tight_layout()
# fig.savefig('../images/Veh_avail_supermarkets_compare_means.jpeg')
plt.show()