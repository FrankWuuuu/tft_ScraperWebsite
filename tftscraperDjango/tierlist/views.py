from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def sayCum (request):
    return render(request, 'cum.html', {'name': 'cummer'})


def getRoutes (request):
    return JsonResponse("cumcumcum", safe = False)
