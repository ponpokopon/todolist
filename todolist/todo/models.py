from django.db import models

# Create your models here.
class ToDo(models.Model):
    """todo"""
    name = models.CharField('タスク名', max_length=255)
    startdate = models.IntegerField('開始日', max_length=255, blank=True)
    deadline = models.IntegerField('期限', max_length=255, blank=True)
    estimate = models.IntegerField('見積もり(日)', max_length=255, blank=True)
    completion = models.IntegerField('完了日', max_length=255, blank=True)
    status = models.IntegerField('ステータス', max_length=255, default=0)

    def __str__(self):
        return self.name


class Completion(models.Model):
    """完了"""
    completion = models.ForeignKey(ToDo, verbose_name='タスク名', related_name='完了日', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment