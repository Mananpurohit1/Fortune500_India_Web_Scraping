#!/usr/bin/env python
# coding: utf-8

# In[48]:


from bs4 import BeautifulSoup
import requests


# In[49]:


url = 'https://www.fortuneindia.com/fortune-500/company-listing/?year=2022&per_page=500&page=1&sort=current-rank&type=asec'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[50]:


print(soup)


# In[51]:


world_titles = soup.find_all('span')


# In[52]:


world_titles


# In[58]:


world_table_titles = [title.text.strip() for title in world_titles]



# Define a list of valid titles
valid_titles = ["2022", "2021", "Change", "Company", "Ownership", "Industry", "Rs cr", "YoY change %",
                "Rs cr", "YoY change %", "Rs cr", "Rank", "YoY change %", "% of total income", "Rs cr",
                "% of Ebitda", "Rs cr", "Rs cr", "(x)", "Rs cr", "Rank", "YoY change %", "Rs cr", "Rank",
                "(%)", "(%)", "(in nos)", "Rank", "RS Crore", "(%)"]

# Filter out unwanted titles
filtered_titles = [title for title in world_table_titles if title in valid_titles]


filtered_titles_without_first_three = filtered_titles[3:]

print(filtered_titles_without_first_three)


# In[59]:


import pandas as pd

df = pd.DataFrame(columns = filtered_titles_without_first_three)

df


# In[60]:


column_data = soup.find_all('tr', attrs={'class':'mpw-tr company-details-row'})


# In[61]:


column_data


# In[62]:


# Initialize an empty list to store rows of data
data_rows = []

# Iterate through the rows of data
for row in column_data:
    # Find all the <td> elements within the current row
    td_elements = row.find_all('td')
    
    # Extract and store the text content of each <td> element with specific class names
    row_data = [td.text.strip() for td in td_elements if td.has_attr('class') ]
    
    # Append the row_data list to the data_rows list
    data_rows.append(row_data)

# Display the resulting list of data rows
for row in data_rows:
    print(row)



# In[64]:



# Create a DataFrame from the data_rows list
df = pd.DataFrame(data_rows, columns = filtered_titles_without_first_three)

# Display the DataFrame
df


# In[65]:


df.to_csv(r'I:\project\fortune_500_india_data.csv', index=False)


# In[ ]:




