import datetime

from django.db import models
from django.utils import timezone

class Entry(models.Model):
    """
    Model for Journal Entries
    """
    entry = models.CharField('Entry', max_length=1000)
    pub_datetime = models.DateTimeField('Date/Time Published')
    pub_loc_long = models.DecimalField('Location Longitude', max_digits=9, decimal_places=6)
    pub_loc_lat = models.DecimalField('Location Lattitue', max_digits=9, decimal_places=6)

    def __str__(self):
        """
        Returns the entry text instead of the object whenever the entry is converted
        to string.
        """
        return self.entry
    
    def was_published_recently(self):
        """
        Returns whether the entry is published within a day.
        """
        return self.pub_datetime >= timezone.now() - datetime.timedelta(days=1)

    def location(self):
        """
        Returns the location in Google Maps readable formatl; if location is not set
        returns False.
        """
        if self.pub_loc_long or self.pub_loc_lat:
            return str(self.pub_loc_long) + ", " + str(self.pub_loc_lat)
        else:
            return False