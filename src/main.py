from views import LoginHandler, IndexHandler, CrearSerie, EditarSerie, BorrarSerie, VerSerie
import webapp2

app = webapp2.WSGIApplication([
        ('/', LoginHandler), 
        ('/index', IndexHandler),
        ('/newSerie', CrearSerie),
        ('/verSerie/([\d]+)', VerSerie),
        ('/editSerie/([\d]+)', EditarSerie),
        ('/deleteSerie/([\d]+)', BorrarSerie)
        ],
        debug=True)

