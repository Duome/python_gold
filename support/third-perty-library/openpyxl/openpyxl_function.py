# -*- coding: utf-8 -*-
__author__ = 'Duome'

"""openpyxl三方库

"""

from openpyxl import *
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

def write_excel():
    wb = Workbook()     # 新建工作簿
    dest_filename = 'empty_book.xlsx'   # 新建工作簿名

    ws1 = wb.active     # 激活工作簿，并创建表单
    ws1.title = "range names"   # 给表达命名
    for row in range(1, 40):    # 设置39行数，若（0，40）&（1,41）为40行
        ws1.append(range(600))  # 设置列内容

    ws2 = wb.create_sheet(title="Pi")
    ws2['F5'] = 3.14            # 设置F列5行数据为3.14

    ws3 = wb.create_sheet(title="Data")
    for row in range(10, 20):
        for col in range(27, 54):
            _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
    print(ws3['AA10'].value)

    wb.save(filename = dest_filename)   # 保存工作簿

def read_excel():
    """读取工作表数据
    """
    wb = load_workbook('E:\\study_python\\python_gold\\project\\excel-rw\\22.xlsx')
    sheets = wb.get_sheet_names()    # 获取有表单名组成的list
    print sheets

def filter_excel():
    """过滤工作表数据
    """
    wb = Workbook()
    ws = wb.active

    data = [
        ["Fruit", "Quantity"],
        ["Kiwi", 16],
        ["Grape", 15],
        ["Apple", 2],
        ["Peach", 30],
    ]

    for r in data:
        ws.append(r)

    # ws.auto_filter.ref = "A1:B1"
    # ws.auto_filter.add_filter_column(0, ["Kiwi", "Apple", "Mango"])
    ws.auto_filter.add_sort_condition("B2:B15")
    print a

    wb.save("filtered.xlsx")

if __name__ == '__main__':
    filter_excel()