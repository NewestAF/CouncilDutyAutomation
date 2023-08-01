import os

from flask import Flask, send_from_directory
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .views import main_views, patrol
    app.register_blueprint(main_views.bp)
    app.register_blueprint(patrol.bp)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app

# app = Flask(__name__)
#
# df = pd.DataFrame()
# connection = sql.connect("student.db")
# df = pd.read_sql('select * from student', connection)
# connection.close()
#
#
# @app.route('/')
# def index():
#     return build_table(df, 'grey_dark', font_size='30px', font_family='Arial', padding='40px',
#                        text_align='center')
#
#     # if __name__ == '__main__':
#
#
# # app.run(host='0.0.0.0', debug=True)
