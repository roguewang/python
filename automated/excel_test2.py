#!/usr/bin/env python
# Author:rogue

import xlsxwriter

workbook = xlsxwriter.Workbook("/tmp/xlsx_test.xlsx")

worksheet = workbook.add_worksheet()

chart = workbook.add_chart({"type": "column"})

title = [u"业务名称", u"星期一", u"星期二", u"星期三", u"星期四", u"星期五", u"星期六", u"星期日", u"平均流量"]

buname = [u"业务官网", u"新闻中心", u"购物频道", u"体育频道", u"亲子频道"]

data = [
    [150, 152, 158, 149, 155, 145, 148],
    [89, 88, 95, 93, 97, 100, 99],
    [250, 252, 258, 249, 255, 245, 248],
    [189, 188, 195, 193, 197, 200, 199],
    [1150, 1152, 1158, 1149, 1155, 1145, 1148],
]

format = workbook.add_format()

format.set_border(1)

format_title = workbook.add_format()

format_title.set_bg_color("#CCCCCC")

format_title.set_align("center")

format_title.set_bold()

format_ave = workbook.add_format()

format_ave.set_border(1)

format_ave.set_num_format("0.00")

worksheet.write_row("A1", title, format_title)

worksheet.write_column("A2", buname, format)

worksheet.write_row("B2", data[0], format)
worksheet.write_row("B3", data[1], format)
worksheet.write_row("B4", data[2], format)
worksheet.write_row("B5", data[3], format)
worksheet.write_row("B6", data[4], format)


def chart_series(cur_row):
    worksheet.write_formula("I" + cur_row, "=AVERAGE(B" + cur_row + ":H" + cur_row + ")", format_ave)

    chart.add_series({
        "categories": "=Sheet1!$B$1:$H$1",
        "values": "=Sheet1!$B$" + cur_row + ":$H$" + cur_row,
        "line": {"color": "black"},
        "name": "=Sheet1!$A$" + cur_row,
    })


for row in range(2, 7):
    chart_series(str(row))

chart.set_size({"width": 577, "height": 287})

chart.set_title({"name":u"业务流量周报图表"})

chart.set_y_axis({"name":"Mb/s"})

worksheet.insert_chart("A8",chart)

workbook.close()
