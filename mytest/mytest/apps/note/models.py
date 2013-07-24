#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class Note(models.Model):
    title = models.CharField(max_length=128, verbose_name=u"Заголовок")
    desc = models.TextField(verbose_name=u"Текст заметки")
    date_time = models.DateTimeField(auto_now=True, verbose_name=u"Дата/Время")

    def __unicode__(self):
        return unicode(self.title)

admin.site.register(Note)
