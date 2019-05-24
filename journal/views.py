from rest_framework import viewsets, mixins
from .serializers import EntrySerializer
from .models import Entry

class EntriesView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()