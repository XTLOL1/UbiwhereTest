# UbiwhereTest
Ubiwhere entry test attempt

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
 - Restrict the way the Speed Tiers are created
 - Add unit tests to test the API and user perms
 - Add a feature that filters the RoadSegments by designation of the last SegmentSpeed reading (Done)
 - Make a guide to setup and run the app
