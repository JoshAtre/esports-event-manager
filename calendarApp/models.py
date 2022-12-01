from django.db import models

class Event(models.Model):
    day = models.DateField("day of event")
    eventTime = models.TimeField("time of event")

    class Meta:
        verbose_name = "Scheduling"
        verbose_name_plural = "Scheduling"
