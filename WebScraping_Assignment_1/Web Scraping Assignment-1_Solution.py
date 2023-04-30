#!/usr/bin/env python
# coding: utf-8

# ### Q1 Write a python program to display all the header tags from wikipedia.org and make data frame
# 

# In[1]:


#importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def wikheaders(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    headers=[]
    for i in soup.find_all(['h1', 'h2','h3','h4','h5','h6']):
        headers.append(i.text)
    
    df = pd.DataFrame({'Header_Tags':headers})
    print(df)
    
    
wikheaders('https://en.wikipedia.org/wiki/Main_Page')


# ### Q2 Write a python program to display IMDB’s Top rated 50 movies’ data (i.e. name, rating, year of release)
# 

# ### and make data frame.

# In[2]:


#importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def IMDB(url): #Function for top 50 movie's name ,ratings and year of release
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #For Movies
     
    selection_class="lister-item-header"
    movie_title_tags=soup.find_all('h3',{'class':selection_class})
    movie_titles=[]

    for tag in movie_title_tags:
        title = tag.find('a').text
        movie_titles.append(title)
    Top50Movies=movie_titles[:50] #Saving top 50 movies names
    
    #For Ratings
    rating_selector="inline-block ratings-imdb-rating"            
    movie_rating_tags=soup.find_all('div',{'class':rating_selector})
    movie_rating_tagss=[]
    for tag in movie_rating_tags:
        movie_rating_tagss.append(tag.get_text().strip())
    Ratings = movie_rating_tagss[:50] #Saving top 50 required ratings of movies
    
    #For Year of Release
    
    year_selector = "lister-item-year text-muted unbold"           
    movie_year_tags=soup.find_all('span',{'class':year_selector})
    movie_year_tagss=[]
    for tag in movie_year_tags:
        movie_year_tagss.append(tag.get_text().strip()[1:5])
    Year=  movie_year_tagss[:50]  #Saving required top 50 movies year of release
 
    
    top50 = pd.DataFrame({'Movie_Name':Top50Movies,'Ratings':Ratings,'Year_Of_Release':Year})
    print(top50)

IMDB('https://www.imdb.com/search/title/?groups=top_250&sort=user_rating')
    


# ### Q3 Write a python program to display IMDB’s Top rated 50 Indian movies’ data (i.e. name, rating, year of
# ### release) and make data frame.

# In[3]:


#importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def IMDBind(url): #Function for top 50 Indian movie's name ,ratings and year of release
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #For Movies
     
    selection_class="titleColumn"
    movie_title_tags=soup.find_all('td',{'class':selection_class})
    movie_titles=[]

    for tag in movie_title_tags:
        title = tag.find('a').text
        movie_titles.append(title)
    Top50Movies=movie_titles[:50]
    
    #For Ratings
    rating_selector="ratingColumn imdbRating"            
    movie_rating_tags=soup.find_all('td',{'class':rating_selector})
    movie_rating_tagss=[]
    for tag in movie_rating_tags:
        movie_rating_tagss.append(tag.get_text().strip())
    Ratings = movie_rating_tagss[:50]
    
    #For Year of Release
    
    year_selector = "secondaryInfo"           
    movie_year_tags=soup.find_all('span',{'class':year_selector})
    movie_year_tagss=[]
    for tag in movie_year_tags:
        movie_year_tagss.append(tag.get_text().strip()[1:5])
    Year=  movie_year_tagss[:50]
 
    
    top50 = pd.DataFrame({'Movie_Name':Top50Movies,'Ratings':Ratings,'Year_Of_Release':Year})
    print(top50)

IMDBind('https://www.imdb.com/india/top-rated-indian-movies/')
    


# ### Q4 Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)
# ### from https://presidentofindia.nic.in/former-presidents.htm and make data frame.

# In[4]:


#importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def president(url):
    page = requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #FormerPresident_Names
    select_class ="presidentListing"
    president_tags=soup.find_all('div',{'class':select_class})
    Names=[]
    
    for tag in president_tags:
        title = tag.find('h3').text.split('(')[0]
        Names.append(title)
    
    
    
    #FormerPresident_TermOfOffice
    
    year_class ="presidentListing"
    term_tags=soup.find_all('div',{'class':year_class})
    Office=[]
    
    for tag in term_tags:
        term_year = tag.find('p').text.split(':')[1]
        Office.append(term_year)
    
    Former_President=pd.DataFrame({'Former_President Name':Names,'Term of Office':Office})
    
    print(Former_President)
    
    
president('https://presidentofindia.nic.in/former-presidents.htm')
    


# ### Q5 Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
# 
# 

# ### a)Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# 

# In[3]:


#importig required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def team(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #top 10 ODI team names
    team=[] #empty list for storing yhe titles
    for i in soup.find_all('span', class_="u-hide-phablet")[:10]:
        team.append(i.text)
    
    #top 10 ODI teams matches
    matches=[]
        #for 1st team
    for i in soup.find('td',class_='rankings-block__banner--matches'):
        matches.append(i.text)
        #for other teams
    for i in soup.find_all('td',class_='table-body__cell u-center-text')[0:18:2]:
        matches.append(i.text)
    
    #top teams rating
    rating =[]
      #for 1st team
    for i in soup.find_all('td',class_='rankings-block__banner--rating u-text-right'):
        rating.append(i.get_text().strip())
        #for other teams
    for i in soup.find_all('td',class_='table-body__cell u-text-right rating')[:9]:
        rating.append(i.text)
    
   
   #Top 10 team names':team,'Matches':matches
    k=pd.DataFrame({'Top 10 team names':team,'Matches':matches,'Rating':rating})
    print(k)
         
team('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# ### b) Top 10 ODI Batsmen along with the records of their team and rating.
# 

# In[62]:


#importig required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def Batsmen(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #top 10 Batsman names
    man=[] #empty list for storing yhe titles
    #for no.1 batsmen
    for i in soup.find_all('div', class_="rankings-block__banner--name")[:1]:
        man.append(i.text)
    #for rest batsman
    findman_tags=soup.find_all('td', class_="table-body__cell name")[:9]
    for tag in findman_tags:
        mann=tag.find('a').text
        man.append(mann)
        
        
    #top 10 ODI Batsman team names
    country=[]
    #for no.1 batsmen
    for i in soup.find_all('div', class_="rankings-block__banner--nationality")[:1]:
        country.append(i.text.split()[0])
    #for rest batsman
    for i in soup.find_all('span',class_='table-body__logo-text')[:9]:
        country.append(i.text)
   

    #top 10 batsman rating
     #for no.1 batsmen
    rating=[]
    for i in soup.find_all('div', class_="rankings-block__banner--rating")[:1]:
        rating.append(i.text.split()[0])
    #for rest batsman
    for i in soup.find_all('td',class_='table-body__cell u-text-right rating')[:9]:
        rating.append(i.text)
    
   
   
    k=pd.DataFrame({'Top 10 Batsman Name':man,'Country':country,'Rating':rating})
    print(k)
         
Batsmen('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')


# ### c) Top 10 ODI bowlers along with the records of their team andrating.

# In[9]:


#importig required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def Bowler(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #top 10 Bowlers names
    man=[] #empty list for storing yhe titles
    #for no.1 bowler
    for i in soup.find_all('div', class_="rankings-block__banner--name")[1:2]:
        man.append(i.text)
    #for rest bowler's
    findman_tags=soup.find_all('td', class_="table-body__cell name")[9:18]
    for tag in findman_tags:
        mann=tag.find('a').text
        man.append(mann)
        
        
    #top 10 ODI Bowler's team names
    country=[]
    #for no.1 bowler
    for i in soup.find_all('div', class_="rankings-block__banner--nationality")[1:2]:
        country.append(i.text.split()[0])
    #for rest bowler's
    for i in soup.find_all('span',class_='table-body__logo-text')[9:18]:
        country.append(i.text)
   

    #top 10 bowler's rating
     #for no.1 bowler's
    rating=[]
    for i in soup.find_all('div', class_="rankings-block__banner--rating")[1:2]:
        rating.append(i.text.split()[0])
    #for rest bowler's
    for i in soup.find_all('td',class_='table-body__cell u-text-right rating')[9:18]:
        rating.append(i.text)
    
   
   
    k=pd.DataFrame({"Top 10 ODI Bowler's Name":man,'Country':country,'Rating':rating})
    print(k)
         
Bowler('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')


# ### Q6 Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
# 

# ### a)Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# 
# 

# In[2]:


#importig required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def Batsmen_name(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #top 10 ODI team names
    team=[] #empty list for storing yhe titles
    for i in soup.find_all('span', class_="u-hide-phablet")[:10]:
        team.append(i.text)
    
    #top 10 ODI teams matches
    matches=[]
        #for 1st team
    for i in soup.find('td',class_='rankings-block__banner--matches'):
        matches.append(i.text)
        #for other teams
    for i in soup.find_all('td',class_='table-body__cell u-center-text')[0:18:2]:
        matches.append(i.text)
    
    #top teams rating
    rating =[]
      #for 1st team
    for i in soup.find_all('td',class_='rankings-block__banner--rating u-text-right'):
        rating.append(i.get_text().strip())
        #for other teams
    for i in soup.find_all('td',class_='table-body__cell u-text-right rating')[:9]:
        rating.append(i.text)
    
   
   #Top 10 team names':team,'Matches':matches
    k=pd.DataFrame({'Top 10 team names':team,'Matches':matches,'Rating':rating})
    print(k)
         
Batsmen_name('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# ### b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# 

# In[12]:


#importig required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def Batsmen(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #top 10 Batsman names
    man=[] #empty list for storing yhe titles
    #for no.1 batsmen
    for i in soup.find_all('div', class_="rankings-block__banner--name")[:1]:
        man.append(i.text)
    #for rest batsman
    findman_tags=soup.find_all('td', class_="table-body__cell name")[:9]
    for tag in findman_tags:
        mann=tag.find('a').text
        man.append(mann)
        
        
    #top 10 ODI Batsman team names
    country=[]
    #for no.1 batsmen
    for i in soup.find_all('div', class_="rankings-block__banner--nationality")[:1]:
        country.append(i.text.split()[0])
    #for rest batsman
    for i in soup.find_all('span',class_='table-body__logo-text')[:9]:
        country.append(i.text)
   

    #top 10 batsman rating
     #for no.1 batsmen
    rating=[]
    for i in soup.find_all('div', class_="rankings-block__banner--rating")[:1]:
        rating.append(i.text.split()[0])
    #for rest batsman
    for i in soup.find_all('td',class_='table-body__cell u-text-right rating')[:9]:
        rating.append(i.text)
    
   
   
    k=pd.DataFrame({'Top 10 Women Batting Name':man,'Country':country,'Rating':rating})
    print(k)
         
Batsmen('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')


# ### c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[1]:


#importig required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def all_rounder(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #top 10 Bowlers names
    man=[] #empty list for storing yhe titles
    #for no.1 bowler
    for i in soup.find_all('div', class_="rankings-block__banner--name")[2:3]:
        man.append(i.text)
    #for rest bowler's
    findman_tags=soup.find_all('td', class_="table-body__cell name")[18:28]
    for tag in findman_tags:
        mann=tag.find('a').text
        man.append(mann)
        
        
    #top 10 ODI Bowler's team names
    country=[]
    #for no.1 bowler
    for i in soup.find_all('div', class_="rankings-block__banner--nationality")[2:3]:
        country.append(i.text.split()[0])
    #for rest bowler's
    for i in soup.find_all('span',class_='table-body__logo-text')[18:28]:
        country.append(i.text)
   

    #top 10 bowler's rating
     #for no.1 bowler's
    rating=[]
    for i in soup.find_all('div', class_="rankings-block__banner--rating")[2:3]:
        rating.append(i.text.split()[0])
    #for rest bowler's
    for i in soup.find_all('td',class_='table-body__cell u-text-right rating')[18:28]:
        rating.append(i.text)
    
   
   
    k=pd.DataFrame({"Top 10 ODI Bowler's Name":man,'Country':country,'Rating':rating})
    print(k)
         
all_rounder('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')


# ### Q7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame
# ### i)Headline
# ### ii) Time
# ### iii) News Link

# In[35]:


#importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

def news(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #For headlines
    headers=[]
    for i in soup.find_all('a',class_='LatestNews-headline'):
        headers.append(i.text)
    
    #for time
    time=[]
 
    for i in soup.find_all('time',class_='LatestNews-timestamp'):
        time.append(i.text)
    #for url
    url=[]
    for i in soup.find_all('a',class_='LatestNews-headline'):
        url.append(i.get('href'))
        
        
    
        
    
    df=pd.DataFrame({'Headline':headers,'Time':time,'News Link':url})
    print(df)
   
news('https://www.cnbc.com/world/?region=world')


# ### Q8Write a python program to scrape the details of most downloaded articles from AI in last 90
# ### days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# ### Scrape below mentioned details and make data frame
# ### i)Paper Title
# ### ii) Authors
# ### iii) Published Date
# ### iv) Paper URL

# In[42]:


#importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

def AI(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.content)
    
    #For Paper titles
    titles=[]
    for i in soup.find_all('h2',class_='sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg'):
        titles.append(i.text)
    #For Authors
    authors=[]
    for i in soup.find_all('span',class_='sc-1w3fpd7-0 dnCnAO'):
        authors.append(i.text)
   
    #For Published Date
    date=[]
    for i in soup.find_all('span',class_='sc-1thf9ly-2 dvggWt'):
        date.append(i.text)
    
    #For URL
    url=[]
    for i in soup.find_all('a',class_='sc-5smygv-0 fIXTHm'):
        url.append(i.get('href'))
    
    df=pd.DataFrame({'Paper Title':titles,'Authors':authors,'Published Date':date,'Paper URL':url})
    print(df)
    
    
    

AI('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
    


# In[ ]:




