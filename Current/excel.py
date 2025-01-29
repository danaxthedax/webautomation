import xlsxwriter
import datetime
import pandas as pd

now = datetime.datetime.now()

workbook = xlsxwriter.Workbook(f"Automation TestResluts {pd.Timestamp.now().strftime('%Y_%m_%d_%H_%M_%S')}.xlsx")
worksheet = workbook.add_worksheet()

date_format = workbook.add_format({'num_format': 'd mmmm yyyy hh:mm'})

test_reslut = [["Chat_test", 1], ["Payment_test", 0], ["lol_test", 1]]

worksheet.write('A1', 'TestResluts')
worksheet.write('B1', now, date_format)

row = 2

cell_passed = workbook.add_format({'bg_color': 'green'})
cell_failed = workbook.add_format({'bg_color': 'red'})


for x in test_reslut:
    worksheet.write(f'A{row}', x[0])
    if x[1] == 1:
        worksheet.write(f'B{row}', "Passed", cell_passed)
    elif x[1] == 0:
        worksheet.write(f'B{row}', "Failed", cell_failed)
    row = row+1
workbook.close()