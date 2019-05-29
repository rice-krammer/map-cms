from rest_framework import serializers
from .models import Entry

from django.utils import timezone

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry

        # Fields to provide to API endpoint
        fields = ('id', 'entry', 'pub_datetime', 'pub_recently', 'pub_location', 'pub_loc_long', 'pub_loc_lat')

        # Arguments for the fields, used to declare whether these are read or write only
        extra_kwargs = {'pub_loc_long': {'write_only': True}, 'pub_loc_lat': {'write_only': True}, 'pub_datetime': {'read_only': True}}

    def create(self, validated_data):
        """
        Overwrites .create() method so that we can verify input and set datetime to current localtime of the server.
        """
        progress, created = Entry.objects.update_or_create(
            entry = validated_data.get('entry', None),
            pub_datetime = timezone.localtime(),
            pub_loc_long = validated_data.get('pub_loc_long', None),
            pub_loc_lat = validated_data.get('pub_loc_lat', None)
        )

        return progress