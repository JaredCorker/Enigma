# from flask import Flask
# from flask import render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     user = {'username': 'Jared'}
#     return render_template('index.html', title = 'Enimga Machine', user = user)

# @app.route('/hello')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug = True)

from app import app