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
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self,lastname):
        self._surname = lastname
        self.required = (".git", "setup.py","README.md","scripts/getting_data.py","scripts/check_repo.py",self.surname+"/__init__.py",self.surname+"/session3.py")


    def check(self):
        """PASSes if repo checks out, FAILs if it does not"""
        for f in self.required:
            if not os.path.exists(f):
                return False

        return True
