from flask import Flask

from convert.routes import convert

app = Flask(__name__)


def run_app():
    app.register_blueprint(convert)

    return app


if __name__ == '__main__':
    run_app().run(debug=True)
