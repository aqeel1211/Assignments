from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd

import requests
title_elements=[]
poster_elements=[]
location_elements=[]
timestamp_elements=[]
URL = "https://realpython.github.io/fake-jobs/"
page=requests.get(URL)
soup=BeautifulSoup(page.content,"html.parser")
job_elements = soup.find_all("div", class_="card-content")
#print (type(job_elements))

for job_element in job_elements:
    
    title_elements.append (job_element.find("h2", class_="title").text.strip())
    poster_elements.append(job_element.find("h3", class_="company").text.strip())
    location_elements.append(job_element.find("p", class_="location").text.strip())
    timestamp_elements.append(job_element.find("time", datetime="2021-04-08").text.strip())
    print (title_elements)
    print (poster_elements)
    print (location_elements)
    print (timestamp_elements)
    print('---',end='\n'*2)

dict = {'name': title_elements, 'poster': poster_elements, 'location': location_elements, 'timestamp': timestamp_elements}  
       
df = pd.DataFrame(dict) 

df.to_csv('GFG.csv',index=False)
