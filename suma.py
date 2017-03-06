#!/usr/bin/python3

import webapp

# Clase suma que hace la suma de dos enteros.
class suma():
    def parse(self, request, rest):
         try:
             operando1 = int(rest.split('/')[1])
             operando2 = int(rest.split('/')[2])
         except ValueError:
             return None
         except TypeError:
             return None
         return (operando1, operando2)

    def process(self, parsedRequest):

         if not parsedRequest:
             return("404 Not found", "<html>" +
                    "<body><h1>No podemos sumar enteros y caracteres.</h1>" +
                    "</body></html>")

         primernum = parsedRequest[0]
         segundonum = parsedRequest[1]
         suma =  primernum + segundonum
         return("200 OK", "<html><body><h1>La suma es: " + str(primernum) +
                "+" + str(segundonum) + "=" + str(suma) +
                "</h1></body></html>")
