# coding=utf-8
# 

import unittest2
from steven_utils.file import getFilenameWithoutPath \
							, getParentFolder
from os.path import join



class TestFile(unittest2.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestFile, self).__init__(*args, **kwargs)


	def testGetFilenameWithoutPath(self):
		self.assertEqual('a.txt', getFilenameWithoutPath(join('C:', 'temp', 'a.txt')))
		self.assertEqual('a.txt', getFilenameWithoutPath('C:\\temp\\a.txt'))
		self.assertEqual('docs', getFilenameWithoutPath('C:\\temp\\docs'))
		self.assertEqual('', getFilenameWithoutPath('C:\\temp\\docs\\'))
		self.assertEqual('a.txt', getFilenameWithoutPath('a.txt'))
		self.assertEqual('a.txt', getFilenameWithoutPath('/tmp/docs/a.txt'))
		self.assertEqual('', getFilenameWithoutPath('/tmp/docs/'))
	
	

	def testGetParentFolder(self):
		self.assertEqual('C:temp', join('C:', 'temp'))
		self.assertEqual('C:temp', getParentFolder(join('C:', 'temp', 'a.txt')))
		self.assertEqual('C:\\temp', getParentFolder('C:\\temp\\a.txt'))
		self.assertEqual('C:\\temp', getParentFolder('C:\\temp\\docs'))
		self.assertEqual('C:\\temp\\docs', getParentFolder('C:\\temp\\docs\\'))
		self.assertEqual('', getParentFolder('a.txt'))
		self.assertEqual('/tmp/docs', getParentFolder('/tmp/docs/a.txt'))
		self.assertEqual('/tmp/docs', getParentFolder('/tmp/docs/'))
	