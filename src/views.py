from datetime import datetime
import os
import webapp2
import jinja2

from webapp2_extras import sessions
from google.appengine.ext import db
from google.appengine.api import users
from models import Serie, Categoria



TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

class BaseHandler(webapp2.RequestHandler):
   
    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))
        
    def checkLogin(self):
        user = users.get_current_user()
        if user:
            return True
        else:    
            urlLogin = users.create_login_url('/')
            return False  

    def getLogout(self):
        user = users.get_current_user()
        if user:
            urlLogout = users.create_logout_url('/')
            return urlLogout        

class LoginHandler(BaseHandler):
    def get(self):
        # El primer if es por si se entroduciese / estando ya logueado
        if self.checkLogin():
            return webapp2.redirect('/index')
        else:
            urlLogin = users.create_login_url('/index')
            self.render_template('login.html', {'url' : urlLogin})

class IndexHandler(BaseHandler):
    def get(self):
        self.checkLogin()
        user = users.get_current_user()
        logoutUrl = self.getLogout();
        
        series = Serie.all()
        categorias = Categoria.all()
        self.render_template('index.html', {'listaSeries' : series, 'categorias' : categorias, 'nickname' : user.nickname(), 'logoutUrl' : logoutUrl })
        
    def post(self):
        cat = Categoria(nombre=self.request.get('inputNewCat'), series=[])
        cat.put()
        # se necesita un sleep ara que los items se creen en el datastore y los vea
        return webapp2.redirect('/index')



class CrearSerie(BaseHandler):
    def get(self):
        self.checkLogin()
        categorias = Categoria.all()
        self.render_template('newSerie.html', {'categorias' : categorias})
        
    def post(self):      
        serie = Serie(nombre=self.request.get('inputNombre'),
                autor=self.request.get('inputAutor'),
                descripcion=self.request.get('inputDescripcion'),
                categorias=self.request.POST.getall('categoriasInput'))
        serie.put()
        print(self.request.POST.getall('categoriasInput'))
        return webapp2.redirect('/index')

    
class BorrarSerie(BaseHandler):  
    def get(self, idSerie):
        iden = int(idSerie)
        serie = db.get(db.Key.from_path('Serie', iden))
        db.delete(serie)
        return webapp2.redirect('/index')


    
           
        
