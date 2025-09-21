from django.db import models

class RoadSegment(models.Model):
    #ended up dropping this cause of problems due to IDs on HyperlinkedModelSerializer
    #pk = models.CompositePrimaryKey("longStartId", "latStartId", "longEndId", "latEndId", primary_key=True)
    longStart = models.FloatField() #models.DecimalField(..., max_digits=3, decimal_places=15)
    latStart = models.FloatField() #models.DecimalField(..., max_digits=2, decimal_places=15)
    longEnd = models.FloatField() #models.DecimalField(..., max_digits=3, decimal_places=15)
    latEnd = models.FloatField() #models.DecimalField(..., max_digits=2, decimal_places=15)
    length = models.FloatField()
    
    class Meta():
        constraints = [
            models.UniqueConstraint(fields=["longStart", "latStart", "longEnd", "latEnd"], name="Unique Road Segments Constraint")
        ]


class SegmentSpeed(models.Model):
    roadSegment = models.ForeignKey(RoadSegment, on_delete=models.CASCADE)
    dateTimeUpdated = models.DateTimeField(auto_now=True)
    speed = models.FloatField()

class SpeedTier(models.Model): #can't allow negatives, can't allow both limits null
    lowerLimit = models.FloatField(default=None, blank=True, null=True) #not inclusive, if not present assume infinite
    upperLimit = models.FloatField(default=None, blank=True, null=True) #inclusive, if not present assume infinite
    designation = models.CharField(max_length=100)
