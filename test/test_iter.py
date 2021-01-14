# coding=utf-8
# 

import unittest2
from steven_utils.iter import firstN, skipN, firstOf, pop, headnRemain



class TestIter(unittest2.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestIter, self).__init__(*args, **kwargs)


	def testFirstN(self):
		self.assertEqual([], list(firstN(0, [1, 2])))
		self.assertEqual([], list(firstN(2, [])))
		self.assertEqual([1], list(firstN(1, [1, 2, 3])))
		self.assertEqual([0, 1], list(firstN(2, range(8))))
		self.assertEqual([1, 2], list(firstN(8, range(1, 3))))
		self.assertEqual([], list(firstN(2, filter(lambda x: x > 5, range(3)))))
		self.assertEqual([], list(firstN(2, filter(lambda x: x > 5, range(3)))))
		self.assertEqual([2, 3], list(firstN(2, filter(lambda x: x > 1, range(8)))))



	def testSkipN(self):
		self.assertEqual([], list(skipN(1, [])))
		self.assertEqual([], list(skipN(3, range(3))))
		self.assertEqual([1, 2], list(skipN(0, [1, 2])))
		self.assertEqual([1, 2], list(skipN(1, range(3))))
		self.assertEqual( [3, 4, 5, 6]
						, list(skipN(3, filter(lambda x: x < 7, range(10)))))
		self.assertEqual( []
						, list(skipN(10, filter(lambda x: x < 7, range(10)))))



	def testFirstOf(self):
		self.assertEqual(3, firstOf(lambda x: x%2 == 1, [2, 4, 3, 1]))
		self.assertEqual('abc', firstOf(lambda x: len(x) > 2, ['xx', '0', 'abc']))
		self.assertEqual(None, firstOf(lambda x: x > 10, range(5)))
		self.assertEqual(None, firstOf(lambda _: True, []))



	def testPop(self):
		self.assertEqual(None, pop([]))
		self.assertEqual(None, pop(filter(lambda x: x < 0, range(3))))
		self.assertEqual(2, pop([2, 3, 4]))

		it = filter(lambda x: x > 2, range(6))
		self.assertEqual(3, pop(it))
		self.assertEqual([4, 5], list(it))



	def testHeadnRemain(self):
		convert = lambda t: (t[0], list(t[1]))

		self.assertEqual( (0, [1, 2, 3, 4])
						, convert(headnRemain(range(5))))

		self.assertEqual( (0, [1, 2, 3, 4])
						, convert(headnRemain([0,1,2,3,4])))

		self.assertEqual( (0, [1, 2, 3, 4])
						, convert(headnRemain(filter( lambda x: x > -1
													, range(-3,5)))))