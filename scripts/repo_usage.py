#!/bin/env python
"""How and when do people commit their code"""


def main():
    """Informative description"""
    import getpass
    from tjarnberg.session4 import orgRepoCommits

    user = raw_input('Github username: ')
    passw = getpass.getpass('Github password: ')

    commits = orgRepoCommits(user,passw)

    commits
    print commits



if __name__ == "__main__":
    main()
