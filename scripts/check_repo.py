#!/usr/bin/env python
"""
Checking directory content with input
"""
import sys, os

def main(argv):
	from tjarnberg.session3 import CourseRepo, repo_dir

	workDir = argv
	lastname = os.path.basename(os.path.normpath(workDir))
	repo = CourseRepo(lastname)


	with repo_dir(workDir):
		if repo.check():
			print "PASS"
		else:
			print "FAIL"



if __name__ == "__main__":
	main(sys.argv[-1])
