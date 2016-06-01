from django.db import models
from datetime import datetime

class ScheduledTraining(models.Model):
    day = models.IntegerField()
    day_text = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    place = models.CharField(max_length=1024, default="")

    def __str__(self):
        return ("ScheduledTraining(%s, %s-%s)" %
                (self.day_text, self.start_time, self.end_time))

    
class Event(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    place = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    
    def __str__(self):
        return ("Event(%s)" % (self.description,))

    
class News(models.Model):    
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length=1024)
    text = models.TextField()

    def __str__(self):
        return "News(%s)" % (self.title,)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class ExternalVideo(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=2048)
    
