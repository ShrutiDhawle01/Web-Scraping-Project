#!/usr/bin/env python
# coding: utf-8

# In[8]:


from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd


# In[3]:


get_ipython().system('pip install pandas')


# In[9]:


url="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=7ec220e8-4f02-4150-9e0b-9e90cf692f4b&as-searchtext=laptop"
response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent,"html.parser")
print(soup.prettify)


# In[15]:


products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
apps = []                #List to store supported apps                
os = []                  #List to store operating system
hd = []                  #List to store resolution
sound = []               #List to store sound output


# In[17]:


for data in soup.findAll('div',class_='_3pLy-c row'):
        names=data.find('div', attrs={'class':'_4rR01T'})
        price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        rating=data.find('div', attrs={'class':'_3LWZlK'})
        specification = data.find('div', attrs={'class':'fMghEO'})
        
        for each in specification:
            col=each.find_all('li', attrs={'class':'rgWa7D'})
            app =col[0].text
            os_ = col[1].text
            hd_ = col[2].text
            sound_ = col[3].text
        products.append(names.text) # Add product name to list
        prices.append(price.text) # Add price to list
        apps.append(app)# Add supported apps specifications to list
        os.append(os_) # Add operating system specifications to list
        hd.append(hd_) # Add resolution specifications to list
        sound.append(sound_) # Add sound specifications to list
        ratings.append(rating.text)   #Add rating specifications to list


# In[19]:


#printing the length of list
print(len(products))
print(len(ratings))
print(len(prices))
print(len(apps))
print(len(sound))
print(len(os))
print(len(hd))


# In[20]:


import pandas as pd
df=pd.DataFrame({'Product Name':products,'Supported_apps':apps,'sound_system':sound,'OS':os,"Resolution":hd,'Price':prices,'Rating':ratings})
df.head(10)


# In[21]:


df.to_csv('products1.csv')


# In[ ]:




