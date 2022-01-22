from scrapper_remoteok import get_jobs_remote
from scrapper_stackoverflow import get_jobs_stack
from scrapper_weworkremotely import get_jobs_wework

def get_jobs(word):
	jobs = get_jobs_remote(word) + get_jobs_stack(word) + get_jobs_wework(word)
	return jobs