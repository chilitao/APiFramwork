# -*- coding:utf-8 -*-
__author__ = '池立涛'
import xlrd
workbook = None
def get_sheet(path, module):
    open_excel(path)
    return get_sheet_bysheetname(module)
def open_excel(path):
     global workbook
     if (workbook == None):
        workbook = xlrd.open_workbook(path, on_demand=True)
def get_sheet_bysheetname(sheetName):
    global workbook
    return workbook.sheet_by_name(sheetName)
def get_content(sheet, row, col):
    return sheet.cell(row, col).value
def release(path):
    global workbook
    workbook.release_resources()
    del workbook
    workbook=None