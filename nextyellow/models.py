from django.db import models
from django.utils import timezone

# Create your models here.
class HitCount(models.Model):
    ip = models.CharField(max_length=15, default=None, null=True)  # ip 주소
    date = models.DateField(default=timezone.now, null=True, blank=True)  # 조회수가 올라갔던 날짜 