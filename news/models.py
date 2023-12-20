from django.db import models
from django.utils import timezone


class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now_add=timezone.now())

    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return self.headline
