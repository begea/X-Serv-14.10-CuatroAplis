#!/usr/bin/python3

import webapp

# Clase aleat que da URLs aleatorias.
class aleat():
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
         import random
         respuesta = random.randint(1, 1000000000000)
         redirect = "http://localhost:1335/aleat/" + str(respuesta)
         return ("200 OK", "<html><body><h1><a href= " + redirect +
                           ">Dame otra URL</a>" + "</h1></body></html>")
