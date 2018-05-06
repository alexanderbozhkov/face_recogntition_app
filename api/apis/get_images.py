import os

from flask import jsonify
from flask_restplus import Resource, Namespace
from database.db import session
from database.models import Images

api = Namespace('Images', description='Uploaded images info')


@api.route('/all')
class GetAllImages(Resource):

    @api.param('name', 'Filter by name')
    @api.doc('list_images')
    def get(self, name=None):
        # TODO: make name filter
        # if name:
        #     all_images = session.query(Images).get(name)
        #     result = []
        #     for img in all_images:
        #         file_path = os.getcwd() + '/database/images/' + img.img_name + '.jpeg'
        #         result.append((img.img_name, file_path))
        #     return jsonify(images=result)
        all_images = session.query(Images).all()
        result = []
        for img in all_images:
            file_path = os.getcwd() + '/database/images/' + img.img_name + '.jpeg'
            result.append({'image_id': img.id, 'image_name': img.img_name, 'image_path': file_path})
        return jsonify(images=result)


@api.route('/<id>')
@api.param('id', 'The image id', required=True)
class GetImage(Resource):

    @api.doc('single_image_info')
    def get(self, id):
        if id:
            img = session.query(Images).get(id)
            if not img:
                return jsonify({'message': 'Image with this id does not exist!'})
            result = []
            file_path = os.getcwd() + '/database/images/' + img.img_name + '.jpeg'
            result.append({'image_id': img.id, 'image_name': img.img_name, 'image_path': file_path})
            return jsonify(images=result)
        return api.abort(404)

