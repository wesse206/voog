import os

from flask import Flask, flash, json, request, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPTokenAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from importtool import ImportTool
from api import APICalls
from connectDB import connectDB

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a random secret key
jwt = JWTManager(app)
apiService = APICalls()

users = {
    "voog": "V00g@ppL0g1n"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username not in users or not check_password_hash(generate_password_hash(users[username]), password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

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

@app.route('/api/', defaults={'path': ''})
@app.route('/api/<path:path>')
@jwt_required()
def api_base(path):
    return jsonify({"message": "API base route"}), 200


@app.route('/api/getTeacherlessLearners')
def getTeacherLessLearnersView():
    TeacherCode = request.args.get('TeacherCode')
    Day = int(request.args.get('Day'))
    return jsonify(apiService.getTeacherlessLearners(TeacherCode, Day))

@app.route('/api/getAbsentTeachers')
def getAbsentTeachersView():
    return jsonify(apiService.getAbsentTeachers())

@app.route('/api/setAbsentTeacher')
def setAbsentTeacherView():
    TeacherCode = request.args.get('TeacherCode')
    Day = int(request.args.get('Day'))
    return jsonify(apiService.setAbsentTeacher(TeacherCode, Day))

@app.route('/api/removeAbsentTeacher')
def removeAbsentTeacherView():
    TeacherCode = request.args.get('TeacherCode')
    Day = int(request.args.get('Day'))
    return jsonify(apiService.removeAbsentTeacher(TeacherCode, Day))

@app.route('/api/getTeacherlessLearnersVoog')
def getTeacherLessLearnersVoogView():
    TeacherCode = request.args.get('TeacherCode')
    Day = int(request.args.get('Day'))
    return jsonify(apiService.getTeacherlessLearnersVoog(TeacherCode, Day))

@app.route('/api/getTeacherlessLearnersBuddy')
def getTeacherLessLearnersBuddyView():
    TeacherCode = request.args.get('TeacherCode')
    Day = int(request.args.get('Day'))
    return jsonify(apiService.getTeacherlessLearnersBuddy(TeacherCode, Day))

@app.route('/api/getVoogTeachers')
def getVoogTeachersView():
    return jsonify(apiService.getVoogTeachers())


if __name__ == '__main__':
    app.run(host='0.0.0.0')