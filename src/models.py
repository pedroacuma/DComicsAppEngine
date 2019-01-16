from google.appengine.ext import db


class Usuario(db.Model):
    email = db.StringProperty(required=True)
    
class Categoria(db.Model):
    series = db.ListProperty(db.Key)
    nombre = db.StringProperty(required=True)
    
class Serie(db.Model):
    categorias = db.ListProperty(db.Key)
    nombre = db.StringProperty(required=True)
    autor = db.StringProperty(required=True)
    descripcion = db.TextProperty(required=True)
    fecha = db.DateTimeProperty(auto_now=True)
    
