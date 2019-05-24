from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is journal.")

def add_entry(request):
    return HttpResponse("You can add entry here.")
