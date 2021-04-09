from django.db import models
from django.urls import reverse


DAYTIME=(
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
    ('N', 'Night'),
)
class Mod(models.Model):
    name = models.CharField(max_length=50)

class Car(models.Model):
    name = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    mods = models.ManyToManyField(Mod)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Driven(models.Model):
    date = models.DateField('driven date')
    miles = models.IntegerField()
    day_time = models.CharField(
        max_length=1,
        choices=DAYTIME,
        default=DAYTIME[0][0]
        )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_day_time_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']