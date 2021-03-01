# coding=utf-8
# 
# File system related API
# 
from os import listdir
from os.path import isfile, isdir, join, split as pathSplit



def getFiles(directory, withDir=False):
	"""
	[String] directory, [Bool] withDir 
		=> [List] file names under that directory. Sub folders are 
				not included.

	if the function is called without the second parameter 'withDir', then 
	file names are without directory, otherwise full path file names are 
	returned.
	"""
	return \
	[join(directory, f) for f in listdir(directory) if isfile(join(directory, f))] \
	if withDir else \
	[f for f in listdir(directory) if isfile(join(directory, f))]
		



def getSubFolders(directory):
	"""
	[String] directory => [List] sub folder names under that directory

	files are not included
	"""
	return [f for f in listdir(directory) if isdir(join(directory, f))]



def getFilenameWithoutPath(file):
	"""
	[String] file name (with or without full path) 
		=> [String] file name without path
	"""
	return pathSplit(file)[1]



def getParentFolder(file):
	"""
	[String] file name with full path 
		=> [String] parent folder of the file
	"""
	return pathSplit(file)[0]



if __name__ == '__main__':
	print(getFiles('.'))		# show local directory files
	print(getSubFolders('.'))	# show local sub directories