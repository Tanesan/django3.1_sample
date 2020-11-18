from django.db import models



class HomeMonitoringIot(models.Model):
    datatype = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    quantity = models.IntegerField()
    # 今後：{id: line UUID}で管理する？
    user_name = models.CharField(max_length=20, default="")


    class Meta:
        managed = False
        db_table = 'home_monitoring_iot'