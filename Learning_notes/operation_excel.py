"""
操作EXCEL
"""
from openpyxl import load_workbook

wb = load_workbook("testcase")  # 创建workbook对象
ws = wb.active  # 打开第一个sheet，创建sheet对象
# ws = wb["test"]    # 打开指定的sheet页
cell = ws.cell(row=1, column=1)    # 定位cell单元格，创建cell对象(代表第一行第一列的单元格)
cell.value  # 获取cell对象的值

wb.save("testcase")
wb.close()