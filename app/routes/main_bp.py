from flask import Blueprint
from app.controllers.MainController import index, login


main_bp = Blueprint('main', __name__)
main_bp.route('/', methods=['GET'])(index)
main_bp.route('/login', methods=['GET'])(login)
