#!/bin/env python
import requests
from pandas import DataFrame, Series
from dateutil import parser

def orgRepoCommits(user,passw,org='pythonkurs'):
	"""
	Returns the commit history for a organisation on github as a data frame
	"""
	repos = requests.get("https://api.github.com/orgs/"+org+"/repos", auth=(user,passw))
	repo_data = repos.json()

	data = []
	for item in repo_data:
		users_repo = requests.get(item[u'commits_url'][:-6], auth=(user,passw))
		if users_repo.ok:
			commits = users_repo.json()
			cmessage = []
			ctime = []
			for commit in commits:
				cmessage.append(commit[u'commit'][u'message'])
				ctime.append(parser.parse(commit[u'commit'][u'author'][u'date']))

			data.append(Series(data = cmessage, index = ctime, name = item[u'name']))

	commitHistory = DataFrame(data).transpose()

	return commitHistory
