'''
Created on Jul 15, 2013

@author: Justin
'''
import csv

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    def utf_8_encoder(unicode_csv_data):
        drinks = []
        for line in unicode_csv_data:
            drinks.append(line)
            print line
        print drinks
        print 'a'
        yield drinks
        
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data), dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        print [unicode(cell, 'utf-8') for cell in row]
        
    

unicode_csv_reader(open('drinklist.csv'))