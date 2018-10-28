import xlrd
import xlwt
import sys, os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


data = xlrd.open_workbook('../dataconfig/case1.xls')
tables = data.sheets()[0]
print(tables.nrows)
print(tables.cell_value(2, 3))
