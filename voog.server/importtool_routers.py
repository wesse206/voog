import os
from flask import Blueprint, render_template, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from importtool import ImportTool

importtool_bp = Blueprint('importtool_bp', __name__)
importAuth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("admin")
}

@importAuth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
      return username

@importtool_bp.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@importAuth.login_required
def importtool_base(path):
    if request.method == 'POST':
        file = request.files.get("file")
        file.save(os.path.join('voog.server','uploads', f'{file.filename}'))
        print('file saved')
        action = request.form['action']
        importtool = ImportTool(f'voog.server/uploads/{file.filename}')
        if action == 'importTimeTable':          
            importtool.importTimeTable()
        elif action == 'importLearners':
            print('starting learner import')
            importtool.importLearners()
        elif action == 'importTeacherCodes':
            importtool.importTeacherCodes()
        elif action == 'generateVoogList':
            importtool.generateVoogList()

        importtool.cleanup()
        os.remove(f'voog.server/uploads/{file.filename}')
            
        
    return render_template('importtool.html')
