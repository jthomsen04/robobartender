'''
Created on Jul 15, 2013

@author: Justin
'''

from modules.apphandler import AppHandler
from main import Drinks

import csv

class db_loader(AppHandler):

    def __init__(self):
        with open('drinklist.csv', 'rb') as d:
            reader = csv.reader(d)
            for row in reader:
                drink = Drinks(d_ID = int(row[0]), 
                        d_name = row[1], 
                        instructions = row[2], 
                        average_rating = float(row[3]), 
                        rating_count = int(row[4]), 
                        rating_total = int(row[5]))
                drink.put()
                    
 
        