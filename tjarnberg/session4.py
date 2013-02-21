#!/bin/env python
import requests
from pandas import DataFrame, Series
from dateutil import parser
import getpass, datetime
from collections import Counter


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
                
            if item[u'name'] != 'pjohansson':
                data.append(Series(data = cmessage, index = ctime, name = item[u'name']))
    
    commitHistory = DataFrame(data).transpose()

    # return data
    return commitHistory

def WorkHabbits(commits):
    """Takes a DataFrame and returns most common day and hour"""
    days = []
    for i in commits.index:
        day = i.strftime("%A")
        days.append(day)
    cd = Counter(days)

    hours = []
    for i in commits.index:
        hours.append(datetime.datetime.time(i).hour)
    ch = Counter(hours)

    day = cd.most_common(2)
    hour = ch.most_common(2)
    return day, hour

def WorkHabbitUser(userData):
    """Takes userdata and returns common commit day and hour"""

    user = userData.dropna()
    days = []
    for i in user.index:
        day = i.strftime("%A")
        days.append(day)
    cd = Counter(days)

    hours = []
    for i in user.index:
        hours.append(datetime.datetime.time(i).hour)
    ch = Counter(hours)

    day = cd.most_common(2)
    hour = ch.most_common(2)
    return day, hour
