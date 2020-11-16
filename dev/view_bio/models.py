from django.db import models


class IoT(models.Model):
    datatype = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    quantity = models.IntegerField(default=0)
    
