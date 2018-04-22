from app_configuration import init_app
from flask import request, render_template

app, image, db = init_app()


@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST' and 'file' in request.files:
        filename = image.save(request.files['file'])
        return filename
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5002)
