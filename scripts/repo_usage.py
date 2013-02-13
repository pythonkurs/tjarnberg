#!/bin/env python
"""How and when do people commit their code"""


def main():
    """Informative description"""
    import getpass, datetime
    from tjarnberg.session4 import orgRepoCommits, WorkHabbits


    user = raw_input('Github username: ')
    passw = getpass.getpass('Github password: ')

    commits = orgRepoCommits(user,passw)

    day, hour = WorkHabbits(commits)

    print day
    print hour



if __name__ == "__main__":
    main()
