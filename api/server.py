from sqlalchemy.exc import IntegrityError
from app_configuration import init_app
from flask import request, render_template, jsonify
from database.api_db import Images

app, image, db = init_app()
# TODO: probably rebuild it with swagger if I feel like it


@app.route('/get_all_images', methods=['GET'])
def get_all_images():
    # TODO return json with all the uploaded images with their names as unique identifier (for now)
    all_images = db.session.query_property(Images).all()
    result = []
    for img in all_images:
        result.append(img.name)
    return jsonify(image_names=result)


@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    # TODO: This mthod will be called after just for upload, the validation will be done after
    # TODO: ... a request to the database to make sure that imagte with that name does not exist already
    if request.method == 'POST' and 'file' in request.files:
        image_name = request.files['file'].filename.split('.')[0]
        if img_name_in_db(image_name):
            image.save(request.files['file'])
            return image_name

    return render_template('index.html'), 400


def img_name_in_db(file_name):
    new_image = Images(img_name=file_name)
    try:
        db.session.add(new_image)
        db.session.commit()
        return True
    except IntegrityError:
        # img_name already exist
        return False

if __name__ == '__main__':
    app.run(port=5004)
