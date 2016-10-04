from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Topic(models.Model):
    # topic that user is learninig about
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        # retrun a string representation of the model
        return self.text

class Entry(models.Model):
    # specific things learned about topics
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # return a string representation of the models
        return self.text[:50] + "..."
