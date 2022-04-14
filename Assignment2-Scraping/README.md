# Assignment2-Scraping
## Installing libraries

Installing requests
```sh
pip install requests
```
Installing Beautiful Soup

```sh
pip install beautifulsoup4
```

---
## Task 1
Scrape the site https://realpython.github.io/fake-jobs/ using BeautifulSoup and find a desired job

---

## Solution of Task 1
- Created a request to the given URL
- Parsed the page content using BeautifulSoup
- Scraped from the page HTML which consisted all of the jobs and created a jobs list
- Searched for the job from the jobs list and printed it


## How to Run
> Note: `cd Assignments/Assignment2-Scraping` is required to follow further instructions 

```sh
python3 task1.py
```

---

## Task 2
Scrape the site https://realpython.github.io/fake-jobs/ using BeautifulSoup and save all of the job titles,job posters,job locations and timestamps in csv file

---

## Solution of Task 2
- Created a request to the given URL
- Parsed the page content using BeautifulSoup
- Created four lists for job title, job poster, job location and timestamp
- Scraped from the page HTML by tags and stored in each list
- Then created a dictionary with its keys (set as columns names) and assigned lists to them as their values
- Converted it to csv


## How to Run
> Note: `cd Assignments/Assignment2-Scraping` is required to follow further instructions 

```sh
python3 task2.py
```