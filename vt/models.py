from django.db import models

class ScheduledTraining(models.Model):
    day = models.IntegerField()
    day_text = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

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

    
