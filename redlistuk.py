import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects

# Set default fonts
plt.rcParams['font.family'] = 'fantasy'
plt.rcParams['font.fantasy'] = ['Impact']

# Set background colour
plt.rcParams['axes.facecolor'] = 'lightsteelblue'

# Set style
plt.style.use('seaborn-pastel')

# Import data of min wages 2016-2021
df=pd.read_csv('redlist.csv', encoding='latin1')

# Load base map
world = gpd.read_file('ne_10m_admin_0_countries')

# Define UK and optimize projection
UK = world[(world['NAME_LONG'] == 'United Kingdom')]
UK = UK.to_crs(epsg=3857)

# Optimize projection and appearance 
world = world[(world['NAME_LONG'] != 'Antarctica') & (world['NAME_LONG'] != 'Greenland')]
world = world.to_crs(epsg=3857)

# Create base map
base = world.plot(color='seagreen', figsize=(16,9), edgecolor='white',linewidth=0.05)

# Merge data and base map
table = world.merge(df, right_on='country_name', left_on='NAME_LONG')

# Plot merged maps
table.plot(ax=base, color='lightcoral', edgecolor='black', linewidth=0.05, legend=False)

# Plot UK on base map with blue color
UK.plot(ax=base, color='darkslateblue', edgecolor='black', linewidth=0.05, legend=False)

# Add title and customize it
title = plt.text(x=0, y=1.5*1e7, s="Red countries on UK's travel list from 4th October",
                 fontsize=22, color='white', horizontalalignment='center', verticalalignment='top')
title.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='black')])

# Add my logo and customize it
txt = plt.text(x=1.1*1e7, y=0.9*1e7, s='@iadoremaps',
                   fontsize=10, color='white',
                   family='Comic Sans MS', rotation=30,
                 fontproperties={'weight':1000, 'variant':'small-caps'}, wrap=True,
                  horizontalalignment='center', verticalalignment='center')
txt.set_path_effects([PathEffects.withStroke(linewidth=1, foreground='black')])

# Add source and customize it
txt = plt.text(x=-2*1e7, y=-0.8*1e7, s='Source: www.gov.uk', fontsize=8, color='white',
                   fontproperties={'weight':1000, 'variant':'small-caps'}, wrap=True,
                  horizontalalignment='left', verticalalignment='bottom')
txt.set_path_effects([PathEffects.withStroke(linewidth=1, foreground='black')])

# Remove labels of axes
plt.xticks([])
plt.yticks([])

# Set boundaries
bounds = world.geometry.bounds
plt.xlim([bounds.minx.min()-0.5*1e6, bounds.maxx.max()+0.3*1e6])
plt.ylim([bounds.miny.min()-0.5*1e6, bounds.maxy.max()+0.7*1e6])

# Plot the map
plt.tight_layout()
plt.show()