from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class UserJournal(models.Model):
    '''用户日志数据表'''
    usr_name = models.CharField(max_length=50, default=None)
    real_name = models.CharField(max_length=50, default=None)
    date = models.DateField(u'日期', auto_now=False)
    work_today = models.CharField(u'今日工作', max_length=200)
    question = models.CharField(u'问题&风险', max_length=200, blank=True)
    plan_tomorrow = models.TextField(u'明日计划')
    process = models.IntegerField(default=0, blank=False)
    time_consumed = models.FloatField(default=4, blank=False)

    def __str__(self):
        return self.work_today
