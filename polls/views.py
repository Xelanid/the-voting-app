from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Tou're at the polls index.")
