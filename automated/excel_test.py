#!/usr/bin/env python
# Author:rogue
import xlsxwriter

workbook = xlsxwriter.Workbook("/tmp/test.xlsx")

worksheet = workbook.add_worksheet("sheet100")

bold = workbook.add_format({"bold":True})

worksheet.write("A1","hello")

worksheet.write("A2","world",bold)

workbook.close()
