
import web
from datetime import datetime
class Cookie:
    def GET(self, nombre):
        try:
          cookie = web.cookies() 
          now = datetime.now() #variable fecha y hora
          visitas = "0"
          print(cookie)
          
          if nombre: #condicion nombre usuario
            web.setcookie("nombre", nombre, expires = " ", domain = None)
          else:
            nombre = "Anónimo" #parametro de nombre
            web.setcookie("nombre", nombre, expires = " ", domain = None)
         #no. visita
          if cookie.get("visitas"):
            visitas = int(cookie.get("visitas")) 
            visitas += 1 
            web.setcookie("visitas", str(visitas), expires = " ", domain = None)
          else:
            web.setcookie("visitas", str(1), expires="", domain=None) 
            visitas = "1" 
          
          return "Cookie:"+" "+" Visitas: " + str(visitas) + "," " "+ "Nombre: " + nombre + "," + " " + "Fecha y Hora Actual: " + str(now)
        except Exception as e:
              return "¡Error!" + str(e.args)