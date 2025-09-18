from django.db import models

class RoadSegments(models.Model):
    pk = models.CompositePrimaryKey("longStart", "latStart", "longEnd", "latEnd")
    longStart = models.DecimalField(..., max_digits=3, decimal_places=15)
    latStart = models.DecimalField(..., max_digits=2, decimal_places=15)
    longEnd = models.DecimalField(..., max_digits=3, decimal_places=15)
    latEnd = models.DecimalField(..., max_digits=2, decimal_places=15)
    length = models.FloatField()

class SegmentSpeeds(models.Model):
    roadSegment = models.ForeignKey(RoadSegments, on_delete=models.CASCADE)
    dateTimeUpdated = DateTimeField(auto_now=True, auto_now_add=True)
    speed = models.FloatField()

class SpeedTiers(models.Model):
    lowerLimit = models.FloatField(default=None, blank=True, null=True) #not inclusive, if not present assume infinite
    upperLimit = models.FloatField(default=None, blank=True, null=True) #inclusive, if not present assume infinite
    designation = models.CharField(max_length=100)
