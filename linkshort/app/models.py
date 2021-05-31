from django.db import models

# Create your models here.
class shorturl(models.Model):
    orignal_url = models.URLField(max_length=700)
    short = models.CharField(max_length=100)
    time_date = models.DateTimeField()

    def __str__(self):
        return self.orignal_url

