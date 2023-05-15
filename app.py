import os
from flask import Flask, redirect
from routes.photos_routes import photos_routes
from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, redirect
from routes.photos_routes import photos_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes

SECRET_KEY =  os.environ.get("FLASK_SECRET_KEY", "Purple Galaxy Test")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(photos_routes, url_prefix='/photos')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

@app.route('/')
def index():
    return redirect('/photos')