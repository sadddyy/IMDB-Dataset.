#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[14]:


#Reading csv file
df = pd.read_csv("D:\imdb_data.csv")
print(df.head().to_markdown(index=False,numalign="left",stralign="left"))
print()


# In[15]:


#printing the shape of the dataset
print("Shape of the Dataset")
print(df.shape)


# In[16]:


#printing the information of the data
print("Info of the dataset")
print(df.info())


# **Questions:-**
# 1. Which movie made the highest profit? Who were its producer and director? Identify the actors in that film.

# In[17]:


top_revenued=df.sort_values(by='revenue',ascending=False)[:1]
top_revenued.head()


# In[18]:


df['crew'].fillna(0,inplace=True)


# In[19]:


def convert_to_lst(string):
    try:
        return eval(string)
    except:
        return np.nan


# In[20]:


df['crew']=df['crew'].apply(convert_to_lst)
df['cast']=df['cast'].apply(convert_to_lst)
df['genres']=df['genres'].apply(convert_to_lst)


# In[21]:


df1=df.copy()


# In[22]:


df1['profit']=df1['revenue']-df1['budget']


# In[23]:


max_profit=df1['profit'].max()


# In[24]:


df2_max=df1[df1['profit']==max_profit].reset_index(drop=True)


# In[25]:


df2_max['crew'][0]


# In[26]:


for i in df2_max['crew'][0]:
    if i["job"] == "Producer" or i["job"] == "Director":
        print(f'{i["job"]}:{i["name"]}')


# In[27]:


df2_max['cast'].iloc[0]


# In[28]:


for i in df2_max['cast'][0]:
    if i["gender"] == 2 :
        print(f'{i["gender"]}:{i["name"]}')


# **Question**:
# 1. Which film has the max ROI

# In[29]:


df1['roi']=(df1['profit']/df1['budget'])*100
df1[['profit','budget','roi']].sort_values(by='roi',ascending=False)
max_roi=df1[df1['roi']!=np.inf]['roi'].max()
df1[df1['roi']==max_roi]


# **Question**:
# 1.  Find out the unique genres of movies in this dataset.

# In[30]:


df2_genre=df1[~df1['genres'].isna()].reset_index(drop=True)


# In[31]:


df2_genre


# In[32]:


list_genre=[]


# In[33]:


for i in range(len(df2_genre)):
    for j in df2_genre['genres'].iloc[i]:
        print(j)
        list_genre.append(j['name'])


# In[34]:


uniques_genres=list(set(list_genre))


# In[35]:


pd.Series(uniques_genres)
pd.DataFrame(uniques_genres,columns=['Genres'])


# **Make a table of all the producers and directors of each movie. Find the top 3 producers who have produced movies with the highest average RoI?**""

# In[36]:


df2_genre=df1[~df1['genres'].isna()].reset_index(drop=True)
df2_genre


# In[37]:


uniques_genres=list(set(list_genre))


# In[38]:


pd.Series(uniques_genres)

pd.DataFrame(uniques_genres,columns=['Genres'])


# In[39]:


## code to consider only those rows of crew which are not null

df2_crew=df1[df1['crew'].notna()]


# In[42]:


def directors_list(dict_prod):
    list_directors=[]
    
    for i in dict_prod:
        if i['job']=='Director':
            list_directors.append(i['name'])
            
    return list_directors


# In[44]:


df2_crew['Directors']=df2_crew['crew'].apply(directors_list)


# In[45]:


df2_crew['Directors']


# **Which actor has acted in the most number of movies? Deep dive into the movies, genres and profits corresponding to this actor.**

# In[46]:


df2_cast=df1[df1['cast'].notna()].reset_index(drop=True)


# In[47]:


list_actors=[]
for i in range(len(df2_cast)):
    dictionary_list=df2_cast['cast'].iloc[i]
    for j in dictionary_list:
        if j['gender']==2:
            list_actors.append(j['name'])


# In[48]:


actors_df=pd.DataFrame(list_actors)
actors_df.value_counts()[0:5]


# In[ ]:




