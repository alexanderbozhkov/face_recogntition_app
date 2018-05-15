import os

from flask_restplus import Resource, Namespace
from database.db import session
from database.models import Images

api = Namespace('Images', description='Uploaded images info')


@api.route('/delete/<id>')
class DeleteImage(Resource):

    def delete(self, id):

        if not id or not id_validator(id):
            return {'message': 'Provide valid id!'}, 400

        img = session.query(Images).get(int(id))

        if not img:
            return {'message': 'Image does not exist'}, 400

        delete_image(img)

        return {'message': 'Image deleted successfully.'}, 200


def id_validator(n):
    try:
        isinstance(int(n), int)
        return True
    except ValueError:
        return False


def delete_image(img):
    try:
        file_path = os.getcwd() + '/database/images/' + img.img_name + '.jpeg'
        session.delete(img)
        session.commit()
        session.close()
        os.remove(file_path)
    except:
        return {'message': 'Something went wrong'}, 500