from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    co2 = models.FloatField(default=0)
    particulate_matter = models.FloatField(default=0)
    voc = models.FloatField(default=0)
    action_taken = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.timestamp} - CO2: {self.co2}ppm"