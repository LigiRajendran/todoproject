from django.db import models

class Timetable(models.Model):
    day=models.CharField(max_length=250)
    task=models.TextField()
    date=models.DateField()
    def __str__(self):
      return self.day