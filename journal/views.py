from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import EntrySerializer
from .models import Entry


def index(request):
    return HttpResponse("This is journal.")

def add_entry(request):
    return HttpResponse("You can add entry here.")

class EntriesView(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()