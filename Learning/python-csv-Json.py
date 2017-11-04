# -*- coding: utf-8 -*-

#import csv
##open file, read data and move data to list format
#exampleFile = open('example.csv')
#exampleReader = csv.reader(exampleFile)
#exampleData = list(exampleReader)
#
#exampleData
##  [['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],
##   ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'],
##   ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'],
##   ['4/10/2015 2:40', 'Strawberries', '98']]
#
##select 1st column of 1st row
#print(exampleData[0][0])
##'4/5/2015 13:34'
#
##select 6th row
#print(exampleData[6][:])
##close file
#exampleFile.close()
#
#
#import csv
#exampleFile = open('example.csv')
#exampleReader = csv.reader(exampleFile)
#
##loop over all rows except 1st one
#for row in exampleReader:
#    if int(exampleReader.line_num) != 1: #avoid headers if there are any
#        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
#
#exampleFile.close()

#import csv
#
##create csv file and create a writer
#outputFile = open('output.csv', 'w', newline='')
## newline = '' for windows or else you get empty row after every row written
#outputWriter = csv.writer(outputFile)
## use delimiter (instead of comma) and lineterminator for special endings
#csvWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')
#
##add following rows
#outputWriter.writerow(['spam','eggs','bacon','ham'])
##writing a string with commas should not be a problem
#outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
#outputWriter.writerow([1, 2, 3.141592, 4])
#
##don't forget to close the file
#outputFile.close()

##convert excel spreadsheets to csv files
#import os, csv
#import openpyxl
#from openpyxl.cell import get_column_letter
#
#os.getcwd()
#os.chdir('C:\\Users\\Malek\\Documents\\Python Projects\\Learning\\excelSpreadsheets')
#
#for excelFile in os.listdir('.'):
#    if excelFile.endswith('.xlsx') or excelFile.endswith('.xlsm') or excelFile.endswith('.xlsb'):
#        wb = openpyxl.load_workbook(excelFile)        
#        for sheetName in wb.get_sheet_names():
#            sheet = wb.get_sheet_by_name(sheetName)
#            
#            csvFileName = excelFile.split('.')[0] + '_' + sheetName + '.csv'
#            print(csvFileName)
#            csvFile = open(csvFileName, 'w', newline='')
#            csvWriter = csv.writer(csvFile)
#            
#            sheetrows = sheet.max_row
#            sheetcol = sheet.max_column
#            sheetcols = get_column_letter(sheetcol)
#            
#            for rowNum in range(1, sheetrows + 1):
#                rowData = []
#                for i in range(1,sheetcol+1):                    
#                    rowData.append(sheet.cell(row=rowNum, column=i).value)
#                    
#                csvWriter.writerow(rowData)
#            
#            csvFile.close()


###using JavaScript Obejct Notation (JSON)
#import json
#
##reading
#stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
#jsonDataAsPythonValue = json.loads(stringOfJsonData)
#jsonDataAsPythonValue
#
##writing
#pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
#stringOfJsonData = json.dumps(pythonValue)
#print(stringOfJsonData)
##'{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'


# data type support:
#string csv & json
#integers csv & json
#floats csv & json
#booleans csv & json
#lists json
#dictionaries json
#noneType json
#objects 
#file objects
#regex objects
#webelement objects

