import sys, os

class CourseRepo(object):
    def __init__(self,surname):
        [workdir,self.surname] = os.path.split(surname)
        self.required = [
            ".git",
            "setup.py",
            "README.md",
            "scripts/getting_data.py",
            "scripts/check_repo.py",
            self.surname+"/__init__.py",
            self.surname+"/session3.py"]

    def print_repo(self):
        print(self.required)



class repo_dir(object):
    def __init__(self, workdir):
        self.curdir = os.getcwd()
        self.workdir = workdir


    def __enter__(self):
        os.chdir(self.workdir)


    def __exit__(self, type, value, traceback):
        os.chdir(self.curdir)
