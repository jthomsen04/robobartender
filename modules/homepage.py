'''
Created on Jul 14, 2013

@author: Justin
'''
from modules.apphandler import AppHandler
from modules.authentication import validate
from main import Users


class HomePage(AppHandler):
    '''
    classdocs
    '''
    def get(self):
        user_id = validate(self.request.cookies.get('user_id'))
        if user_id:
            user = Users.get_by_id(int(user_id))
            
            self.render('logged-in.html', username = user.u_name)
        else:
            user = None
            self.render('logged-out.html')
    
    def post(self):
        pass

'''
from modules.base import AppHandler
from modules.authentication import validate
from main import Users

class MainPage(AppHandler):    
    def get(self):
        user_id = validate(self.request.cookies.get('user_id'))
        if user_id:
            user = Users.get_by_id(int(user_id))
            self.render('casino_front_in.html', username = user.username)
        else:
            user = None
            self.render('casino_front_out.html')
    
    def post(self):
        self.redirect('/newbj')
'''