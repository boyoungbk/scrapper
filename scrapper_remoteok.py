import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def extract_job(html):
  title = html.find("h2", {"itemprop": "title"}).get_text(strip=True)
  company = html.find("h3", {"itemprop": "name"}).get_text(strip=True)
  job_url = html.find("a", {"itemprop": "url"})["href"]
  return {
    "title": title,
    "company": company,
    "url": f"https://remoteok.com{job_url}"
  }

def extract_jobs(url):
  jobs = []
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("tr", {"class": "job"})
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs

def get_jobs_remote(word):
  url = f"https://remoteok.com/remote-{word}-jobs"
  jobs = extract_jobs(url)
  return jobs
