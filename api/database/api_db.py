from app_configuration import init_app

db = init_app()[1]


class UploadedImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_name = db.Column(db.String(80), nullable=False, unique=True)

    def __init__(self, img_name):
        self.img_name = img_name
