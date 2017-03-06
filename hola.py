#!/usr/bin/python3

import webapp

# Clase hola que dice "¡HOLA!".
class hola():
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        respuesta = "HOLA."
        return ("200 OK", "<html><body><h1>" + respuesta +
                          "</h1></body></html>")

# Clase adios que dice "¡ADIOS!".
class adios():
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        respuesta = "ADIOS."
        return ("200 OK", "<html><body><h1>" + respuesta +
                          "</h1></body></html>")
