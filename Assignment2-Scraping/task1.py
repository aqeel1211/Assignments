from bs4 import BeautifulSoup
import requests
URL = "https://realpython.github.io/fake-jobs/"
page=requests.get(URL)
soup=BeautifulSoup(page.content,"html.parser")
# results = soup.find(id="ResultsContainer") #returns tag
# print (type(results))
# print (results.prettify())


job_elements = soup.find_all("div", class_="card-content")
print (type(job_elements)) #returns resultset
# print (job_elements)
# for job_element in job_elements:
#     print(job_element, end="\n"*4)
#     print (type(job_element)) #prints all the tags

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
    
#     print(title_element.text.strip())
#     print(end="\n"*4)
for job_element in job_elements:
    python_jobs = job_element.find("h2", string="Ship broker")
    #print(type((python_jobs)))
    # if type(python_jobs) is NoneType:
    desired_job=str(python_jobs)
    #print (type(desired_job))
    if desired_job !='None':
        print(desired_job.text)
        #or
        # soup=BeautifulSoup(desired_job,'html.parser')
        # des_job=soup.find(string="Ship broker")
        # print(des_job)