from django.db import models


class IOT(models.Model):
    datatype = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.datatype} at {self.pub_date}"


"""
from django.utils import timezone
current_year = timezone.now()
obj = IOT()
obj.datatype = "curtain"
obj.pub_date = current_year
obj.quantity = 1
obj.save()
"""
    
