from django.db import models
from datetime import datetime
# Create your models here.


class Hotpoint(models.Model):
    #sn = models.CharField(max_length=17, default=datetime.now().strftime("%Y%m%d") + '001', editable=False)
    sn = models.DateTimeField(default=datetime.now())
    top1 = models.CharField(max_length=30)
    top2 = models.CharField(max_length=30)
    top3 = models.CharField(max_length=30)
    top5 = models.CharField(max_length=30)
    top6 = models.CharField(max_length=30)
    top4 = models.CharField(max_length=30)
    top7 = models.CharField(max_length=30)
    top8 = models.CharField(max_length=30)
    top9 = models.CharField(max_length=30)
    top10 = models.CharField(max_length=30)

    def __str__(self):
        return self.top1
