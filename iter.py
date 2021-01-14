# coding=utf-8
# 
# Utility functions to use with iterators or list processing.
#
# More useful functions can be found in python3 itertools package.
# 
from itertools import dropwhile, chain, count
from functools import reduce



"""
	[Int] n (n > 0), [Iterable] it => [Iterable] first n elements
	
	When the iterable it has at least n elements, the function returns
	an iterable object on those n elements;

	When the iterable it has less than n elements, the function returns
	an iterable object on all the elements in it, including the case
	when it has zero elements.
"""
firstN = lambda n, it: \
	map( lambda t: t[1]
	   , filter( lambda t: t[0] < n
	   		   , zip(count(0), it)))



"""
	[Int] n (n > 0), [Iterable] it 
		=> [Iterable] remaining elements after skipping the first
						n elements
	
	When the iterable it has at least n elements, the function returns
	an iterable object on the remain elements;

	When the iterable it has less than n elements, the function returns
	an iterable object with zero elements.
"""
skipN = lambda n, it: \
	map( lambda t: t[1]
	   , filter( lambda t: t[0] > n
	   		   , zip(count(1), it)))



def pop(it):
	"""
	Non-pure function (it consumes the iterator)

	[Iterable] it => [Object] first element in it, if empty return None.
	"""
	iterator = iter(it)
	try:
		return next(iterator)
	except StopIteration:
		return None


# To maintain backward compatibility. Previously the name was "head",
# but a better name for the function is "pop"
head = pop



def headnRemain(it):
	"""
	Non-pure function (it consumes the iterator)

	[Iterable] it => 
		[Object] first element in it
		[Iterable] remaining elements in it

	Throws ValueError when the input iterator is empty
	"""
	iterator = iter(it)
	try:
		return next(iterator), iterator
	except StopIteration:
		raise ValueError



"""
	[Function] func (x -> Bool, where x is an element of it,
	[Iterable] it
	=> [Object] x

	Where x is the first object in it that make the function func
	return True. If it is empty or all elements make the function
	return False, then return None.
"""
firstOf = lambda func, it: \
	pop(dropwhile(lambda x: not func(x), it))



def numElements(it):
	"""
	[Iterable] it => [Integral] number of elements in an interable (it).
	
	This function is not pure, because it changes the input, i.e., consumes 
	the iterator.
	
	The idea comes from:
	https://stackoverflow.com/questions/3345785/getting-number-of-elements-in-an-iterator-in-python
	"""
	# return sum([1 for _ in it])
	return sum(map(lambda _: 1, it))