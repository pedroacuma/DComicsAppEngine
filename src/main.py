from views import LoginHandler, IndexHandler, CrearSerie
import webapp2

app = webapp2.WSGIApplication([
        ('/', LoginHandler), 
         ('/index', IndexHandler),
         ('/newSerie', CrearSerie)
        ],
        debug=True)

