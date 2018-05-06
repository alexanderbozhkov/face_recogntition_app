
# image_upload_app
This is an app for a project that uses facial recognition software for images.

Initialisation of the app at it current state:

1. virtualenv -p python3 venv
2. pip3 install -r api/requirements.txt 
3. cd api/
(app must be run from this dir)
4. python3 database/models.py
(to create new database)
5. python3 app.py <port>
(if no value is provided app will run on port 5000 by default)
