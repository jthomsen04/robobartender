'''
Created on Jul 15, 2013

@author: Justin
'''

from modules.apphandler import AppHandler
from main import Drinks

class DB_Loader(AppHandler):

    def get(self):
        self.render("loader_page.html")
        
    
    def post(self):
        drinklist = [[1,"Allegheny","shake with cracked ice, strain, garnish",0.0,0,0], 
                     [2,"Anchors Aweigh", "shake with cracked ice or blend",0.0,0,0],
                     [3,"Black Dog", "stir with cracked ice, strain into ice cubes",0.0,0,0], 
                     [4,"Blended Comfort", "blend with cracked ice, serve over ice cubes, garnish with peach slices",0.0,0,0]]
        for line in drinklist:
            drink = Drinks(d_ID = int(line[0]), 
                        d_name = line[1],
                        instructions = line[2], 
                        average_rating = float(line[3]), 
                        rating_count = int(line[4]), 
                        rating_total = int(line[5]))
            drink.put()
        