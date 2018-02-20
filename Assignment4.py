
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **weather phenomena** (see below) for the region of **Brandon, Florida, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Brandon, Florida, United States** to Ann Arbor, USA. In that case at least one source file must be about **Brandon, Florida, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Brandon, Florida, United States** and **weather phenomena**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **weather phenomena**?  For this category you might want to consider seasonal changes, natural disasters, or historical trends.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[16]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import seaborn as sns
get_ipython().magic('matplotlib notebook')
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def lightning_comparision():
    #lightning data
    years = ['2000', '2001','2002','2003','2004','2005','2006','2007','2008','2009']
    year_filter = '|'.join(years)
    df_lightning = pd.read_csv('lightning_usa_2000_2010.csv')
    df_lightning['STATE'] = df_lightning['STATE_ABBR'].map(states)
    df_lightning.drop(['STATE_ABBR', 'EVENT_ID', 'DAMAGE_PROPERTY_NUM'], axis=1, inplace=True)
    df_lightning['BEGIN_DATE'] = df_lightning['BEGIN_DATE'].str.split('/').str[-1]
    df_lightning = df_lightning[df_lightning['BEGIN_DATE'].str.contains(year_filter)]
    df_grouped = df_lightning.groupby(df_lightning['BEGIN_DATE']).sum()
    state_list = list(states.values())
   
    
    
    #plane crash data
    df_plane = pd.read_csv('Airplane_Crashes.csv')
    st_filter = '|'.join(state_list)
    df_plane = df_plane[df_plane['Location'].str.contains(st_filter).fillna(True)]
    df_plane = df_plane[~df_plane['Location'].str.contains('Rep').fillna(True)]
    df_plane['Location'] = df_plane['Location'].str.split(', ' ).str[-1]
    df_plane['Date'] =  df_plane['Date'].str.split('/').str[-1]

    total_deaths = df_plane.groupby(df_plane['Date']).sum()
    total_crashes = df_plane.groupby(df_plane['Date']).size()
    df_crashes = pd.DataFrame(total_crashes, columns=['Count'])
    df_crash = total_deaths.merge(df_crashes, how='outer', left_index=True, right_index=True)
    df_crash['Percentage'] = (df_crash['Fatalities']/df_crash['Count'])*100
    
    #count Dataframe
    count = df_lightning.groupby(df_lightning['BEGIN_DATE']).size()
    df_count = pd.DataFrame(count, columns=['COUNT'])
    df_ltning = df_grouped.merge(df_count, how='outer', left_index=True, right_index=True)
    df_ltning['Percentage'] = (df_ltning['DEATHS_DIRECT']/df_ltning['COUNT'])*100

    #Convert Dates
    df_plane = df_plane.set_index('Date')
    crash_dates = pd.to_datetime(df_plane.index.tolist()).strftime('%d%m%Y')
    df_lightning = df_lightning.set_index('BEGIN_DATE')
    lightning_dates = pd.to_datetime(df_lightning.index.tolist()).strftime('%d%m%Y')
    
    
    #plotting the Data
    fig = plt.figure(figsize=(10,7))
    fig.suptitle('Comparing the Lighting Strike and \nAirplane Crash Occurrences and Deaths from 2000-2009', color='black', fontsize=14)
    plt.style.use('dark_background')

    
  
    #left Plot
    plt.subplot(121)
    count_plane_plot = plt.plot(years, df_crash['Count'], '-', color='lime', lw=2)
    count_lightning_plot = plt.plot( years, df_ltning['COUNT'], '-', color='deepskyblue', lw=2)
    plt.gca().fill_between(range(2000,2010), df_crash['Count'], df_ltning['COUNT'], facecolor='lightskyblue', alpha='.3')
    ax = plt.gca()
    xticks = (pd.date_range('1/1/2000', '12/31/2009', freq='AS') + pd.Timedelta('1D')).strftime('%Y').astype(int) 
    ax.set_xticks(xticks)
    ax.set_xticklabels(years, rotation=45, ha='center', color='black', fontsize=10)
    ax.tick_params(axis='y', colors='black')
    plt.grid(True, linestyle='--', linewidth=.5)
    plt.ylabel('Number of Occurrences', color='black', fontsize=14)
    
    #Right Plot
    plt.subplot(122)
    plane_deaths_plot = plt.plot(years, df_crash['Fatalities'], '-', color='red', lw=2)
    lightning_death_plot = plt.plot(years, df_ltning['DEATHS_DIRECT'], '-', color='orange', lw=2)
    plt.gca().fill_between(range(2000,2010), df_crash['Fatalities'], df_ltning['DEATHS_DIRECT'], facecolor='yellow', alpha='.3')
    ax1 = plt.gca()
    xticks = (pd.date_range('1/1/2000', '12/31/2009', freq='AS') + pd.Timedelta('1D')).strftime('%Y').astype(int) 
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(years, rotation=45, ha='center', color='black', fontsize=10)
    ax1.tick_params(axis='y', colors='black')




    plt.ylabel('Number of Deaths', color='black', fontsize=14)
    plt.tight_layout()
    plt.subplots_adjust(bottom=.15, top=.9)
    fig.text(.5, .04, 'Year', color='black', ha='center', fontsize=14)
    fig.text(.9, .26, 'Plane\n Deaths', color='red', fontsize=11)
    fig.text(.80, .16, 'Lightning Deaths', color='orange', fontsize=11)
    fig.text(.4, .65, 'Lightning \n  Strikes', color='deepskyblue', fontsize=11)
    fig.text(.4, .21, 'Plane\n Crashes', color='lime', fontsize=11)
    plt.grid(True, linestyle='--', linewidth=.5)
    
    return 
lightning_comparision()


# In[ ]:




# In[ ]:



