from flask import *
import os
import json

from online_shopping.helpers import JSONEncoder


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)
    app.json_encoder = JSONEncoder
    # app.logger.debug('app.config = %s', app.config)

    # try:
    #     os.major(app.instance_path)
    # except OSError:
    #     pass

    # @app.route('/')
    # def main():
    #     return render_template('blog/start.html')

    from online_shopping import db
    db.init_app(app)

    from online_shopping import admin
    from online_shopping import api
    from online_shopping import store
    app.register_blueprint(store.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(api.bp)

    app.add_url_rule('/', endpoint='index')
    return app
