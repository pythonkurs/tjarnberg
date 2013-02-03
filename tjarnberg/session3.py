import sys, os

class ContextDir(object):
    """Changeing directory within this context."""
    def __init__(self, workdir):
        self.curdir = os.getcwd()
        self.workdir = workdir


    def __enter__(self):
        os.chdir(self.workdir)


    def __exit__(self, type, value, traceback):
        os.chdir(self.curdir)


class CourseRepo(object):
    """Check repository structure in dir"""
    def __init__(self,dir):
        if dir is "":
            print("No directory give, using current directory")
            dir = os.getcwd()

        [workdir,lastname] = os.path.split(dir)
        self.surname = lastname

    @property
    def surname(self,lastname):
        self.required = (".git", "setup.py","README.md","scripts/getting_data.py","scripts/check_repo.py",lastname+"/__init__.py",lastname+"/session3.py")

    def check(self):
        """PASSes if repo checks out, FAILs if it does not"""
        for file in self.require:
            if not os.path.exist(file):
                retrun "FAIL"

        retrun "PASS"

    def print_repo(self):
        print(self.required)
