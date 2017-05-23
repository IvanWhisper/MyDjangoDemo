from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    #字段显示
    class Meta:
        verbose_name='问题'
        verbose_name_plural='问题列表'
    #内容显示
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.pub_date<=now


class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    class Meta:
        verbose_name='选择'
        verbose_name_plural='选择列表'
    def __str__(self):
        return self.choice_text




