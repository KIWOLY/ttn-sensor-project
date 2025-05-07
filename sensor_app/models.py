from django.db import models

class SensorData(models.Model):
    alcohol = models.FloatField()
    benzene = models.FloatField()
    co2 = models.FloatField()
    coord_lat = models.FloatField()
    coord_lon = models.FloatField()
    humidity = models.FloatField()
    nox = models.FloatField()
    pressure = models.FloatField()
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SensorData at {self.created_at}"