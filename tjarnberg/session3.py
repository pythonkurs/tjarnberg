import sys, os

class repo_dir(object):
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
    def __init__(self,lastname):
        if dir is "":
            sys.stderr.write("No surname given.")
            sys.exit(-1)
        self.surname = lastname


    @property
    def required(self):
        return (".git", "setup.py","README.md","scripts/getting_data.py","scripts/check_repo.py",self.surname+"/__init__.py",self.surname+"/session3.py")


    def check(self):
        """PASSes if repo checks out, FAILs if it does not"""
        for file in self.required:
            if not os.path.exists(file):
                return False

        return True
