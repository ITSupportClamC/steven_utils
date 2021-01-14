# coding=utf-8
# 

import unittest2
from steven_utils.excel import fromExcelOrdinal, getRawPositionsFromFile \
							, fileToLines, getRawPositionsFromLines
from steven_utils.iter import skipN
from steven_utils.utility import currentDir
from toolz.functoolz import compose
from functools import partial
from datetime import datetime
from os.path import join



class TestExcel(unittest2.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestExcel, self).__init__(*args, **kwargs)


	def testGetRawPositionsFromFile(self):
		file = join(currentDir(), 'samples', 'Thomson Reuters fund pricing 2021-01-08.xlsx')
		positions = list(getRawPositionsFromFile(file))
		self.assertEqual(2, len(positions))
		self.verifyPosition(positions[1])



	def testGetRawPositionsFromFile2(self):
		file = join(currentDir(), 'samples', 'Bloomberg fund pricing 2021-01-08.xlsx')
		positions = compose(
			list
		  , getRawPositionsFromLines
		  , partial(skipN, 7)
		  , fileToLines
		)(file)
		self.assertEqual(2, len(positions))
		self.verifyPosition2(positions[1])



	def verifyPosition(self, position):
		self.assertEqual(7, len(position))
		self.assertEqual('HK0000664489', position['ISIN Code'])
		self.assertEqual( 'China Life Franklin Global-Short Term Bond I USD'
						, position['Name'])
		self.assertEqual('USD', position['Currency'])
		self.assertAlmostEqual(9.9888, position['NAV per share'])
		self.assertAlmostEqual(248941791.98, position['Fund Size'])
		self.assertAlmostEqual(244945873.74, position['Class Assets'])
		self.assertAlmostEqual(24521823.7879, position['Shares Outstanding'])



	def verifyPosition2(self, position):
		self.assertEqual(11, len(position))
		self.assertEqual( datetime(2021,1,8)
						, fromExcelOrdinal(position['DATE (MM/DD/YYYY)']))
		self.assertEqual( 'CLSTFIU HK Equity'
						, position['BLOOMBERG CODE / ISIN / SEDOL'])
		self.assertEqual('CHINA LIFE FR ST BOND-I USD', position['FUND NAME'])
		self.assertEqual('USD', position['CURRENCY'])
		self.assertAlmostEqual(9.9888, position['NAV'])
		self.assertEqual('', position['BID'])
		self.assertEqual('', position['OFFER'])
		self.assertAlmostEqual(248941791.98, position['FUND SIZE (Actual)'])
		self.assertAlmostEqual(244945873.74, position['CLASS ASSETS (Actual)'])
		self.assertAlmostEqual(24521823.7879, position['SHARE OUT (Actual)'])
		self.assertEqual('', position['FIRM ASSETS UNDER MANAGEMENT (Actual)'])