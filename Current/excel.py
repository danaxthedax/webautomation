import xlsxwriter
import datetime



workbook = xlsxwriter.Workbook('Automation_TestResluts.xlsx')
worksheet = workbook.add_worksheet()

now = datetime.datetime.now()
date_format = workbook.add_format({'num_format': 'd mmmm yyyy hh:mm'})

test_reslut = [["Chat_test", 1], ["Payment_test", 0]]

worksheet.write('A1', 'TestResluts')
worksheet.write('B1', now, date_format)



workbook.close()