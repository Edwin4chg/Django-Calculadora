from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def sumar(request, num1, num2):
    resultado = num1 + num2
    return HttpResponse(f'La suma de {num1} + {num2} = {resultado}')

def restar(request, num1, num2):
    resultado = num1 - num2
    return HttpResponse(f'La resta de {num1} - {num2} = {resultado}')

def multiplicar(request, num1, num2):
    resultado = num1 * num2
    return HttpResponse(f'La multiplicación de {num1} * {num2} = {resultado}')