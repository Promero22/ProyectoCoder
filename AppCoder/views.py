from django.shortcuts import render

# Create your views here.
def Curso(self):

      Curso =  Curso(nombre="Desarrollo web", camada="19881")
      Curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)
