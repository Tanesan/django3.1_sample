from django.db import models


class HomeMonitoringIot(models.Model):
    datatype = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'home_monitoring_iot'