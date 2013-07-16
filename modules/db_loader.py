'''
Created on Jul 15, 2013

@author: Justin
'''

from modules.apphandler import AppHandler
from main import Drinks

import csv

class DB_Loader(AppHandler):

    def get(self):
        
        self.render("loader_page.html")
        
        def unicode_csv_reader(unicode_csv_data="drinklist.csv", dialect=csv.excel, **kwargs):
            # csv.py doesn't do Unicode; encode temporarily as UTF-8:
            csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),dialect=dialect, **kwargs)
            for row in csv_reader:
                # decode UTF-8 back to Unicode, cell by cell:
                yield [unicode(cell, 'utf-8') for cell in row]

            def utf_8_encoder(unicode_csv_data):
                for line in unicode_csv_data:
                    drink = Drinks(d_ID = int(line[0]), 
                        d_name = line[1],
                        instructions = line[2], 
                        average_rating = float(line[3]), 
                        rating_count = int(line[4]), 
                        rating_total = int(line[5]))
                    drink.put()
        unicode_csv_reader()

        