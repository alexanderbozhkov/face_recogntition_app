import os
import logging
from flask import request
from flask_restplus import Resource, Namespace
from flask_uploads import UploadSet, IMAGES
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from werkzeug.datastructures import FileStorage
from database.db import session
from database.models import Images


api = Namespace('Images', description='Uploaded images info')

post_parser = api.parser()
post_parser.add_argument('image_file', type=FileStorage, location='files')
post_parser.add_argument('name', location='form', type='string', required=True)
image = UploadSet('images', IMAGES)
post_parser = api.parser()
UPLOAD_FOLDER = os.getcwd() + '../database/'
image = UploadSet('images', IMAGES)
post_parser = api.parser()

post_parser.add_argument('image_file', type=FileStorage, location='files')
post_parser.add_argument('name', location='form', type='string', required=True)

logging.basicConfig(
  level=logging.DEBUG,
  format="%(levelname)s: %(asctime)s {%(filename)s:%(lineno)d}: %(message)s "
)


@api.route('/upload')
class UploadImage(Resource):

    @api.expect(post_parser, validate=True)
    def post(self):
        if not request.files.getlist("image_file"):
            return {'message': 'File is required'}, 400
        for uploaded_file in request.files.getlist("image_file"):
            input_filename = os.path.basename(uploaded_file.filename)
            allowed_extensions = {".jpeg"}
            if not is_extension_allowed(input_filename, allowed_extensions):
                message = {
                    "message": "Only these extensions are allowed: %(exts)s, but filename is %(input_filename)s" % dict(
                        exts=str(allowed_extensions), input_filename=input_filename),
                }
                logging.error(message)
                return message, 400
            else:
                image_name = request.values["name"]
                if img_name_in_db(image_name):
                    image.save(request.files['image_file'], name=image_name + '.jpeg')
                    return {'Uploaded image': image_name}, 201
        return {'message': 'Image with this name already exists.'}, 400


def is_extension_allowed(filename, allowed_extensions_with_dot):
    [fname, ext] = os.path.splitext(filename)
    return ext in allowed_extensions_with_dot


def img_name_in_db(file_name):
    new_image = Images(img_name=file_name)

    try:
        session.add(new_image)
        session.commit()
        return True
    except(IntegrityError, InvalidRequestError):
        # img_name already exist
        return False
    finally:
        session.close()
