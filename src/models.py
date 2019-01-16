from google.appengine.ext import db


class Usuario(db.Model):
    email = db.StringProperty(required=True)
    
class Categoria(db.Model):
    nombre = db.StringProperty(required=True)
    series = db.ListProperty(db.Key)


class Serie(db.Model):
    nombre = db.StringProperty(required=True)
    autor = db.StringProperty(required=True)
    descripcion = db.TextProperty(required=True)
    fecha = db.DateTimeProperty(auto_now=True)
    
    @property
    def categorias(self):
        return Categoria.gql("WHERE series = :1", self.key())    