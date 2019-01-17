from views import LoginHandler, IndexHandler, CrearSerie, EditarSerie, BorrarSerie
import webapp2

app = webapp2.WSGIApplication([
        ('/', LoginHandler), 
         ('/index', IndexHandler),
         ('/newSerie', CrearSerie),
         ('/editSerie/([\d]+)', EditarSerie),
         ('/deleteSerie/([\d]+)', BorrarSerie)
        ],
        debug=True)

