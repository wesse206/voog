import os

from flask import Flask, request, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash

from api_routes import api_bp, auth
from importtool_routers import importtool_bp

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Api users
users = {
    "voog": generate_password_hash("HSDVoog2025")
}

# Basic auth for the API
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
      return username

# Angular app
@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('./voog/dist/voog/browser', path)

@app.route('/')
def root():
  return send_from_directory('./voog/dist/voog/browser', 'index.html')

# All /api/ routes are in the blueprint
app.register_blueprint(api_bp, url_prefix='/api')
# The entire importtool is in the blueprint, using seperate website design (Material 3)
app.register_blueprint(importtool_bp, url_prefix='/importtool')

if __name__ == '__main__':
    app.run(debug=True)