#!/usr/bin/env python
# encoding: utf-8

# DO WPROWADZANIA ZMIAN W KONTENERZE:
# docker-compose -d --build
# docker-compose up

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import *
from app.routes import *
from app.tests.flask_test import test_start


# initialize application
app = Flask(__name__)
app.config.from_object("app.config.Config")

# initialize database
db.init_app(app)
migrate = Migrate(app, db)

# register model blueprints containing endpoints
app.register_blueprint(main_bp)

# initialize login manager
#login_manager = LoginManager(app)
#login_manager.login_view = 'main.login'

''' notka
   Aby stworzyć bazę danych:
      / docker-compose exec web flask shell

   A w konsoli:

      from app import db

      db.drop_all()
      db.create_all()
      db.session.commit()
   Dodawanie rezerwacji
      db.session.add(Reservation(price=555, status='reservation status', client_id=None, employee_id = None, offer_id = None))
'''

# HOME -> defined in main_bp
#@app.route('/', methods=['GET'])
#def index():
#   return jsonify(hello="Hello from home")

# CONVENIENCE FOR DEVELOPING. DELETE LATER
@app.route('/clear',methods=['GET'])
def clearall():
   db.drop_all()
   db.create_all()
   db.session.commit()
   return "DATABASE CLEARED\n"

# CONVENIENCE FOR DEVELOPING. DELETE LATER
@app.route('/test',methods=['GET'])
def testall():
   test_start()
   return "DATABASE TESTED\n"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
