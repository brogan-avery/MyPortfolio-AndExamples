from django.db import models

# these are items I know that I eat so I have entered them in via the admin dashboard
class Food_items(models.Model):
    item = models.CharField(max_length=400)
    cals = models.IntegerField()
    group = models.CharField(max_length=400)

    def __str__(self):
        return str(self.cals)

class Consumption(models.Model):
    item = models.CharField(max_length=400)
    cals = models.IntegerField()
    date = models.CharField(max_length=400)

    def __str__(self):
        return str(self.date)




