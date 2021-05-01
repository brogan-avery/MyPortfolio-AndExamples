from django.db import models

# can only be changed by admin
class Actions(models.Model):
    action = models.CharField(max_length=400)
    cat = models.CharField(max_length=400) # category of exercise activity: endurance, strength, or flexibility
    targetArea = models.CharField(max_length=400) # targeted muscles or body parts (ex: calves, biceps, cardio)

    # def __str__(self):
    #     return str(self.cals)

class Plan(models.Model):
    name = models.CharField(max_length=400)
    action = models.CharField(max_length=400)
    time = models.IntegerField()
    reps = models.IntegerField()
    order = models.IntegerField() # this is mostly unused so far

    def __str__(self):
        return str(self.name)