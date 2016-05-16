from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypassword@localhost/PensonData'
app.secret_key = 'mypassword'
from views import *
if __name__ == '__main__':
    app.run(debug=True)
