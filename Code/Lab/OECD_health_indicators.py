"""
OECD health statistics  

Links
* http://www.oecd.org/health/health-systems/health-data.htm 

Prepared for Data Bootcamp course at NYU  
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab 

Written by Dave Backus, January 2016 
Created with Python 3.5 
"""
"""
import packages, check versions 
"""
import sys 
import pandas as pd 
#import matplotlib.pyplot as plt

print('\nPython version: ', sys.version) 
print('Pandas version: ', pd.__version__, '\n') 

#%%
"""
read data from OECD 
"""
url1 = 'http://www.oecd.org/health/health-systems/'
url2 = 'OECD-Health-Statistics-2015-Frequently-Requested-Data.xls'

# healthcare spending 
hc = pd.read_excel(url1+url2, 
                   skiprows=3, sheetname=1, index_col=0, 
                   na_values=['..']) 

# select years 
hc = hc[list(range(1980,2014))]
# select countries and transpose df 
countries = ['Canada', 'France', 'Germany', 'Japan', 'United Kingdom', 
             'United States']
some = hc[hc.index.isin(countries)].T

# plot 
ax = some.plot(lw=2, subplots=False)
ax.set_title('Healthcare spending', fontsize=14, loc='left')
ax.set_ylabel('Percent of GDP')
ax.legend(loc='upper left', fontsize=10, handlelength=2, labelspacing=0.15)

#%%
"""
Plot number of docs 
"""
# number of docs 
docs = pd.read_excel(url1+url2, 
                   skiprows=3, sheetname='Physicians', index_col=0,
                   skip_footer=21, 
                   na_values=['..']) 

# select years 
docs = docs[[2012]]
# mpd.columns = map(str.rstrip, mpd.columns)
docs.index = [name.rsplit(maxsplit=1)[0] for name in docs.index.tolist()]

# select countries 
countries = ['Canada', 'France', 'Germany', 'Japan', 'United Kingdom', 
             'United States']
some = docs[docs.index.isin(countries)]

# plot 
ax = some.plot(kind='barh', alpha=0.5, legend=False) 
ax.set_title('Number of doctors', fontsize=14, loc='left') 
ax.set_xlabel('Number of Doctors per 1000 Population') 

