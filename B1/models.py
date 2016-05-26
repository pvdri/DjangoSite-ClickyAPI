from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Analytics(models.Model):
    si = models.URLField(max_length=128, unique=True)
    ip = models.CharField(max_length=128)
    org = models.CharField(max_length=128)
    #
    # def __unicode__(self):
    #     return self.si

# ip = item["ip_address"]
# si = item["session_id"]
# org = item["organization"]
