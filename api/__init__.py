from flask import Flask, jsonify

def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        app.config.from_mapping(test_config)

    @app.route('/')
    def root():
        return (jsonify(''), 204)

    return app
