# UbiwhereTest
Ubiwhere entry test attempt

## How to Run

If you're using Linux, you can just run the ```setupLinux.sh``` script and everything will be setup automatically.
If you're using Windows, **untested script**, run the ```setupWindows.bat``` script and everything should be setup automatically.
### DO NOT RUN THE SCRIPTS WHEN NOT ON THE REPOSITORIES BASE FOLDER, THEY DO NOT USE ABSOLUTE PATHS

If for some reason the scripts above do not work, following these steps:
A virtual environment was used to run this program, I recommend you do the same.
To install the dependencies, run:
```
pip install -r requirements.txt
```
Then to seed the database, run the following shell script:
```
./seedDatabase.sh or ./seedDatabase.bat
```

After that, everything should be setup, you can now run the API using the following shell script or ```python manage.py runserver```:
```
./run.sh or ./run.bat
```




#### Checklist used during development
 - Setup Project (done, using SQLite, idk how to do PostgreSQL, i tried though)
 - Setup App (done)
 - Setup Rest Framework (done)
 - Setup Users and Admin panel (Done)
 - Setup Permission Groups (Done)
 - Do Endpoint permission verification (Not needed, added to default perms in settings.py)
 - Create DTO Models (Done)
 - Create Serializers (Done)
 - Create Views (Done, need to change the get a bit though to add the designation limit labels)
   - Add number of Speed readings on RoadSegments (Done)
   - Add string designation to SegmentSpeed get based on the media speed (Done)
   - Add way to lookup SegmentSpeeds in specific RoadSegment (Done, /findRoadSegment/startLong/startLat/endLong/endLat/)
 - Find a way to populate database from csv file (Done, python manager.py seedDatabase)
 - Setup Swagger (Done)
 - Restrict the way the Speed Tiers are created (Done, made it so that you can't create or delete, can only update or patch)
 - Add unit tests to test the API and user perms (Done, wrote some tests to validate perms and algorithms in SpeedTiers endpoints)
 - Add a feature that filters the RoadSegments by designation of the last SegmentSpeed reading (Done)
 - Make a guide to setup and run the app (You're reading it :) )
