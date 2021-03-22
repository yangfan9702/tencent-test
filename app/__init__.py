from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from elasticapm.contrib.flask import ElasticAPM


from .setting import config
from .blueprint import index_bp
from .task import celery

apm = ElasticAPM()


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500


def register_blueprints(app):
    app.register_blueprint(index_bp)


def create_app():
    app = Flask('app')
    db = SQLAlchemy()
    app.config.from_object(config)

    db.init_app(app)
    register_errors(app)
    register_blueprints(app)
    apm.init_app(app)

    return app


flask_app = create_app()


