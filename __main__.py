import os

from flask import Flask, request, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

from api_routes import api_bp, auth
from importtool_routers import importtool_bp

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

users = {
    "voog": generate_password_hash("HSDVoog2025")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
      return username

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/api/uploadfile', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         files = request.files.getlist("file")  
#         # Iterate for each file in the files List, and Save them 
#         for file in files:
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], f'{file.filename}'))
#             importtool = ImportTool(f'{file.filename}')
#             importtool.importTimeTable()
#             importtool.cleanup()
#             os.remove(f'{file.filename}')
#         return redirect(url_for('upload_file'))
#     return '''
#     <!doctype html>
#     <title>Upload a file to import</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file multiple>
#       <input type=submit value=Upload>
#     </form>
#     '''

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('./voog/dist/voog/browser', path)

@app.route('/')
def root():
  return send_from_directory('./voog/dist/voog/browser', 'index.html')

# All /api/ routes are in the blueprint
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(importtool_bp, url_prefix='/importtool')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)