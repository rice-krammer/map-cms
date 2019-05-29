from rest_framework import viewsets, mixins
from .serializers import EntrySerializer
from .models import Entry

# REST Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EntriesView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    
    # Initializing the serializer
    serializer_class = EntrySerializer

    # Setting the permission
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Setting the queryset
    queryset = Entry.objects.all().order_by('-id')