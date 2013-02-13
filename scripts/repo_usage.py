#!/bin/env python
"""How and when do people commit their code"""
from tjarnberg.session4 import orgRepoCommits, WorkHabbits, WorkHabbitUser


def main():
    """Informative description"""
    import getpass

    user = raw_input('Github username: ')
    passw = getpass.getpass('Github password: ')

    commits = orgRepoCommits(user,passw)

    day, hour = WorkHabbits(commits)

    print "Most common commit days and hours for class"
    print day
    print hour

    return commits

if __name__ == "__main__":
    commits = main()
    print "maximum number of commits for users= "
    print commits.count().max()
    
    uday, uhour = WorkHabbitUser(commits['tjarnberg'])
    print "Most common commit days and hours for me"
    print uday
    print uhour

    uday, uhour = WorkHabbitUser(commits['alneberg'])
    print "Most common commit days and hours for alneberg"
    print uday
    print uhour

    uday, uhour = WorkHabbitUser(commits['hugerth'])
    print "Most common commit days and hours for hugerth"
    print uday
    print uhour
