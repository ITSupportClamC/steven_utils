# coding=utf-8
# 
# Some utility functions to read Excel in Python.
#
# The toolz and xlrd package must be installed.
#
from toolz.functoolz import compose
from xlrd import open_workbook
from datetime import datetime, timedelta
from functools import partial
from itertools import takewhile
from utils.iter import headnRemain



def fromExcelOrdinal(ordinal, _epoch0=datetime(1899, 12, 31)):
	"""
	[Float] ordinal => [datetime] date

	In Excel, an date is represented by a float number (ordinal), where the
	integral part represents the date and the decimal part represents the time
	of that day. This function converts that number to a python datetime object.

	Code sample comes from:

	https://stackoverflow.com/questions/29387137/how-to-convert-a-given-ordinal-number-from-excel-to-a-date
	"""
	if ordinal > 59:
		ordinal -= 1
	return (_epoch0 + timedelta(days=ordinal)).replace(microsecond=0)



def worksheetToLines(ws):
	"""
	[Worksheet] ws => [Iterable] ([List]) lines	
	
	if numColumns is None, then we will use the number of columns
	given in the sheet.
	"""
	cellValue = lambda ws, row, column: \
		ws.cell_value(row, column)

	rowToList = lambda ws, row: \
		list(map(partial(cellValue, ws, row), range(ws.ncols)))

	return map(lambda row: partial(rowToList, ws), range(ws.nrows))



def fileToLines(file):
	"""
	[String] file => [Iterable] lines

	Read an Excel file, convert its first sheet into lines, each line is
	a list of the columns in the row.
	"""
	return worksheetToLines(open_workbook(file).sheet_by_index(0))



def getRawPositionsFromLines(lines):
	"""
	[Iterator] ([List]) lines => [Iterator] ([Dictionary]) positions
	"""
	stripIfString = lambda x: x.strip() if isinstance(x, str) else x

	# [List] line => [List] headers
	getHeaders = compose(
		list
	  , partial(takewhile, lambda x: x != '')
  	  , partial(map, stripIfString)
	)


	# [List] headers, [List] line => [Dictionary] position
	toPosition = lambda headers, line: compose(
		dict
	  , partial(zip, headers)
	  , partial(map, stripIfString)
	)(line)


	emptyLine = lambda line: \
		len(line) == 0 or stripIfString(line[0]) == ''


	return \
	compose(
		lambda t: map( partial(toPosition, t[0])
					 , takewhile( lambda line: not emptyLine(line)
					 			, t[1])
					 )
	  , headnRemain
	)(lines)



"""
	[String] file => [Iterator] positions

	Assume file is an Excel file, this function reads its first worksheet and
	convert the lines from that worksheet to positions.
"""
getRawPositionsFromFile = compose(
	getRawPositions  
  , fileToLines
)