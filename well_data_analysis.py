#!/usr/bin/env python
# coding: utf-8

# ##### *Import Libraries*

# In[1]:



import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
matplotlib.rcParams['figure.figsize'] = (20,10)


# ##### *Load Data Set*

# In[2]:


well_data = pd.read_csv('./796_wells_lat_long.csv')
well_data.head()


# In[3]:


# basic statistical description of the data
well_data.describe()


# ##### *Clean Data Set*

# In[4]:


# setting column names for easy referencing
convenient_column_names = ['R_date','Lat','Lon','1995','2000','2005','2010','2015']
well_data.columns = convenient_column_names
well_data.describe()


# In[5]:


# making a function that returns a data set containing valid ie not null values of a certain year
def clean_data(column,df=well_data):
    columns_to_keep = ['Lat','Lon',column]
    out_df = df.copy().loc[:,columns_to_keep]
    out_df = out_df[out_df[column].notna()]
    out_df = gpd.GeoDataFrame(out_df, geometry=gpd.points_from_xy(out_df['Lon'], out_df['Lat']))
    return out_df
    


# In[6]:


clean_data('1995')


# In[7]:


# storing cleaned data in a dictionary named df for easy future use
df = dict((x,clean_data(x)) for x in convenient_column_names[3:])


# 
# ---
# 
# ### Load Bangladesh Shape file

# In[38]:


# Plot map of Bangladesh
bd_map_ax = gpd.read_file('./Bangladesh.shp').plot(edgecolor='black', color='white')


# In[66]:


# plot well data of 1995 on map of Bangladesh
well_points_1995 = df['1995'].loc[:,['1995','geometry']].plot(color='red', marker='+',ax=bd_map_ax)
well_points_1995.set_title('1995');
fig = well_points_1995.get_figure()

# Now converting this work-flow to a function for rest data
def generate_plot(column_name,geometry_col='geometry',df=df,country_ax=bd_map_ax):
    da = df[column_name].copy()
    well_points = da.loc[:,[column_name,geometry_col]].plot(color='red', marker='+',ax=country_ax)
    well_points.set_title(column_name);
    fig = well_points.get_figure()
    return fig


# In[94]:


# Store every figures in another dictionary
for x in convenient_column_names[3:]:
    print(x)
    generate_plot(x).show()


# In[ ]:





# In[ ]:





# In[ ]:




