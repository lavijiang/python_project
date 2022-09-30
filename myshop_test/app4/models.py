from django.db import models

# Create your models here.
class UserBaseInfo(models.Model):
    id = models.AutoField(_("编号"),primary_key=True)
    username = models.CharField(_("用户名"), max_length=30)
    password = models.CharField(_("密码"), max_length=20)
    status = models.CharField(_("状态"), max_length=50)
    createdate = models.DateTimeField(_("创建日期"), db_column='createDate')
    def __str__(self):
        return str(self.id)
    class Meta:
        managed = False
        verbose_name = '人员基本信息'
        db_table = 'UserBaseInfo4'
    