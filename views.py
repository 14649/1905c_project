from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
       return HttpResponse("index")


def login(request):
       return redirect("/index")


def res(request):
       return HttpResponse("res")

def add_car(request):
       return HttpResponse("add_car")