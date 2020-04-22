from django.db import models

class Member(models.Model):
    
    id = models.CharField(primary_key=True,max_length=100)
    real_name = models.CharField(max_length=256)
    tz = models.CharField(max_length=256)

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    members = models.ForeignKey(Member, related_name= 'activity_periods', on_delete=models.CASCADE)





