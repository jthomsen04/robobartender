'''
Created on Jul 14, 2013

@author: Justin
'''

import os
from webapp2 import WSGIApplication, Route
from google.appengine.ext import db

root_dir = os.path.dirname(__file__)
template_dir = os.path.join(root_dir, 'templates')

class Users(db.Model):
    u_name = db.StringProperty(required = True)
    p_hash = db.StringProperty(required = True)
    email = db.StringProperty(required = True)
    
class Drinks(db.Model):
    d_name = db.StringProperty(required = True)
    instructions = db.TextProperty(required = True)
    rating = db.IntegerProperty(required = False)

class Ingredients(db.Model):
    i_name = db.StringProperty(required = True)
    
class Measurements(db.Model):
    d_id = db.IntegerProperty(required = True)
    i_id = db.IntegerProperty(required = True)
    quantity = db.IntegerProperty(required = True)
    measurement = db.StringProperty(required = True)
    
class Reviews(db.Model):
    u_id = db.IntegerProperty(required = True)
    d_id = db.IntegerProperty(required = True)
    rating = db.IntegerProperty(required = True)
    review = db.TextProperty(required = False)
    
class Favorites(db.Model):
    u_id = db.IntegerProperty(required = True)
    d_id = db.IntegerProperty(required = True)
    rating = db.IntegerProperty(required = False)

app = WSGIApplication([
        Route(r'/', handler='modules.homepage.HomePage', name='homepage'),
        Route(r'/login', handler='modules.authentication.Login', name='login'),
        Route(r'/signup', handler='modules.authentication.SignUp', name='signup'),
        Route(r'/logout', handler='modules.authentication.LogOut', name='logout')], 
        debug=True)

'''
# Create the WSGI application and define route handlers
app = WSGIApplication([
        Route(r'/', handler='modules.mainpage.MainPage', name='mainpage'),
        Route(r'/login', handler='modules.authentication.Login', name='login'),
        Route(r'/signup', handler='modules.authentication.SignUp', name='signup'),
        Route(r'/logout', handler='modules.authentication.Logout', name='logout'),
        Route(r'/newbj', handler='modules.game.NewBlackjack', name='newbj'),
        Route(r'/insurancebj', handler='modules.game.InsuranceBlackjack', name='insurancebj'),
        Route(r'/loseins', handler='modules.game.LoseInsurance', name='loseins'),
        Route(r'/playbj', handler='modules.game.PlayBlackjack', name='playbj'),
        #Route(r'/resetchips', handler='modules.game.ResetChips', name='resetchips'),
        Route(r'/resultsbj', handler='modules.game.ResultsBlackjack', name='resultsbj')], 
        debug=True)
'''


#if __name__ == '__main__':
#    pass