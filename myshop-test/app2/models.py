from django.db import models

# Create your models here.
class UserBaseInfo(models.Model):
    id = models.AutoField(verbose_name='编号',primary_key=True)
    status = models.CharField(verbose_name='状态',max_length=1)