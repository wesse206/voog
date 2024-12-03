import os

from flask import Flask, flash, json, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

from ImportTool import ImportTool
from api import APICalls
from connectDB import connectDB

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
apiService = APICalls()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist("file")  
        # Iterate for each file in the files List, and Save them 
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f'{file.filename}'))
            importtool = ImportTool(f'{file.filename}')
            importtool.importTimeTable()
            importtool.cleanup()
            os.remove(f'{file.filename}')
        return redirect(url_for('upload_file'))
    return '''
    <!doctype html>
    <title>Upload a file to import</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file multiple>
      <input type=submit value=Upload>
    </form>
    '''

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
    print(TeacherCode, Day)
    return jsonify(apiService.getTeacherlessLearnersVoog(TeacherCode, Day))


if __name__ == '__main__':
    app.run()