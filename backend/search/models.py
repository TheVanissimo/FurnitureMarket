from django.db import models


class Location(models.Model):
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.region}, {self.city}, {self.street} {self.house}"


class Furniture(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    width_cm = models.FloatField()
    height_cm = models.FloatField()
    depth_cm = models.FloatField()

    photo_path = models.FileField(upload_to='images/', blank=True, null=True)
    color = models.CharField(max_length=50)

    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='furniture_items')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
