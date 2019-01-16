from google.appengine.ext import db


class Usuario(db.Model):
    email = db.StringProperty(required=True)
    
class Categoria(db.Model):
    nombre = db.StringProperty(required=True)
    
    # Definirlo asi evita que tengamos que anadir a mano cada vez que se crea una serie
    @property
    def series(self):
        return Serie.gql("WHERE categorias = :1", self.key())    

class Serie(db.Model):
    nombre = db.StringProperty(required=True)
    autor = db.StringProperty(required=True)
    descripcion = db.TextProperty(required=True)
    fecha = db.DateTimeProperty(auto_now=True)
    categorias = db.ListProperty(db.Key)

    
    
