from flask import Flask

app = Flask(__name__)

def create_app():
    return app

if __name__ == '__main__':
    app = create_app()

    app.run(debug=True)