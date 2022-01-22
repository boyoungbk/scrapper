from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("remoteJobs")

db = {}

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/report")
def report():
	word = request.args.get("word", str)
	if word:
		word = word.lower()
		existing_jobs = db.get(word)
		if existing_jobs:
			jobs = existing_jobs
		else:
			try:
				jobs = get_jobs(word)
				db[word] = jobs
			except:
				return redirect("/none")
	else:
		return redirect("/")
	return render_template("report.html", count=len(jobs), searching_by=word, jobs=jobs)

@app.route("/none")
def none():
	return render_template("none.html")

@app.route("/export")
def export():
	try:
		word = request.args.get("word")
		if not word:
			raise Exception()
		word = word.lower()
		jobs = db.get(word)
		if not jobs:
			raise Exception()
		save_to_file(jobs)
		return send_file("jobs.csv")
	except:
		return redirect("/")

app.run(host="0.0.0.0")
