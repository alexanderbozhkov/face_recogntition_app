
# image_upload_app
This is an app for a project that uses facial recognition software for images.

Initialisation of the app at it current state:

1. virtualenv -p python3 venv
2. pip3 install -r api/requirements.txt 
3. cd api/
4. python3
5. (in python shell) from database.api_db import db
6. db.create_all()
(exit python shell)
7. python3 api/server.py 
(on port 5004)
