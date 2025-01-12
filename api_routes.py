from flask import Blueprint, jsonify, request, url_for
from flask_httpauth import HTTPBasicAuth

from api import APICalls

global auth 
auth = HTTPBasicAuth()

api_bp = Blueprint('api_bp', __name__)
apiService = APICalls()

@api_bp.route('/', defaults={'path': ''})
@api_bp.route('/<path:path>')
@auth.login_required
def api_base(path):
    return jsonify({"message": "API base route"}), 200

@api_bp.route('/getTeacherlessLearnersVoog')
@auth.login_required
def getTeacherlessLearnersVoogView():
    TeacherCode = request.args.get('TeacherCode')
    Day = int(request.args.get('Day'))
    return jsonify(apiService.getTeacherlessLearnersVoog(TeacherCode, Day))

@api_bp.route('/getTeacherlessLearnersBuddy')
@auth.login_required
def getTeacherlessLearnersBuddyView():
    TeacherCode = request.args.get('TeacherCode')
    Day = int(request.args.get('Day'))
    return jsonify(apiService.getTeacherlessLearnersBuddy(TeacherCode, Day))

@api_bp.route('/getAbsentTeachers')
@auth.login_required
def getAbsentTeachersView():
    return jsonify(apiService.getAbsentTeachers())

@api_bp.route('/setAbsentTeacher')
@auth.login_required
def setAbsentTeacherView():
    TeacherCode = request.args.get('TeacherCode')
    Day = int(request.args.get('Day'))
    return jsonify(apiService.setAbsentTeacher(TeacherCode, Day))

@api_bp.route('/getVoogTeachers')
@auth.login_required
def getVoogTeachersView():
    return jsonify(apiService.getVoogTeachers())

@api_bp.route('/removeAbsentTeacher')
@auth.login_required
def removeAbsentTeacherView():
    TeacherCode = request.args.get('TeacherCode')
    Day = int(request.args.get('Day'))
    return jsonify(apiService.removeAbsentTeacher(TeacherCode))