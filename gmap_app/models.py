from django.db import models

class Places(models.Model):
    address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100, default='')
    longitude = models.CharField(max_length=100, default='')
    
    def __unicode__(self):
        return self.address
