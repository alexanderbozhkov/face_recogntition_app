from app_configuration import init_app
from flask import request, render_template

app, image, db = init_app()
# TODO: probably rebuild it with swagger if I feel like it


@app.route('/get_all_images', methods=['GET'])
def get_all_images():
    # TODO return json with all the uploaded images with their names as unique identifier (for now)
    return 'todo'


@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    # TODO: This mthod will be called after just for upload, the validation will be done after
    # TODO: ... a request to the database to make sure that imagte with that name does not exist already
    if request.method == 'POST' and 'file' in request.files:
        filename = image.save(request.files['file'])
        return filename
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5004)
