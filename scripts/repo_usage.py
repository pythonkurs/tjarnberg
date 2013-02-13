#!/bin/env python
"""How and when do people commit their code"""


def main():
    """Informative description"""
    import getpass, datetime
    from tjarnberg.session4 import orgRepoCommits
    from collections import Counter

    user = raw_input('Github username: ')
    passw = getpass.getpass('Github password: ')

    commits = orgRepoCommits(user,passw)

    c = Counter(range(1:7))

    for i in commits.index
        c
        # days.append(datetime.date.isoweekday(i))



if __name__ == "__main__":
    main()
