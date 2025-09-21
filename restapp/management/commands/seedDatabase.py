from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from restapp.models import RoadSegment, SegmentSpeed, SpeedTier
from csv import reader

class Command(BaseCommand):
    help = "Used to seed the database with the Traffic-Speed submodule"

    #index 1 = Long_start
    #index 2 = Lat_start
    #index 3 = Long_end
    #index 4 = Lat_end
    #index 5 = Length
    #index 6 = registered Speed

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "something123!")
        if SpeedTier.objects.all().count() == 0:
            lowerTier = SpeedTier(upperLimit=20, designation="elevada") # <= 20
            lowerTier.save()
            midTier = SpeedTier(lowerLimit=20, upperLimit=50, designation="média") # > 20 && <= 50
            midTier.save()
            higherTier = SpeedTier(lowerLimit=50, designation="baixa") # > 50
            higherTier.save()
        with open("Traffic-Speed/traffic_speed.csv") as csvfile:
            csv_reader = reader(csvfile, delimiter=',')
            for row in csv_reader:
                try:
                    road = RoadSegment.objects.filter(longStartId=row[1], latStartId=row[2], longEndId=row[3], latEndId=row[4])
                    if not road.exists():
                        road = RoadSegment(longStartId=row[1], latStartId=row[2], longEndId=row[3], latEndId=row[4], length=row[5])
                        road.save()
                    segmentSpeed = SegmentSpeed(roadSegment=road, speed=row[6])
                    segmentSpeed.save()
                except:
                    print(f"Died on line: {csv_reader.line_num}")

                
