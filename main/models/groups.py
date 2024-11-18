from django.db import models
from main.models.categories import Category


class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    chat_id = models.BigIntegerField(unique=True, verbose_name='Chat ID')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Category ID')

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.title
