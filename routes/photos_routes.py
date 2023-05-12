from flask import Blueprint
from controllers.photos_controller import index, new, create, edit, update, delete, comment

photos_routes =  Blueprint('photos_routes', __name__)

photos_routes.route('/')(index)
photos_routes.route('/new')(new)
photos_routes.route('', methods=["POST"])(create)
photos_routes.route('/<id>/edit')(edit)
photos_routes.route('/<id>', methods=["POST"])(update)
photos_routes.route('/<id>/delete', methods=["POST"])(delete)
photos_routes.route('/<id>/comment', methods=["POST"])(comment)