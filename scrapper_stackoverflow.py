"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def get_last_page(url):
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
  last_page = int(pages[-2].get_text(strip=True))
  return last_page

def extract_job(html):
  title = html.find("h2").find("a")["title"]
  company = html.find("h3").find("span", recursive=False).get_text(strip=True)
  job_id = html["data-jobid"]
  return {
    "title": title,
    "company": company,
    "url": f"https://stacoverflow.com/jobs/{job_id}"
  }

def extract_jobs(last_page, url):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{url}&pg={page+1}", headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs_stack(word):
  url = f"https://stackoverflow.com/jobs?q={word}"
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page, url)
  return jobs
