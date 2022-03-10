from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    # def __str__(self):
    #     return f"{self.name}: room {self.room} on floor {self.room_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.title} at {self.start_time} on {self.date}"
# Create your models here.



