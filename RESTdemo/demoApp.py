from flask import Flask
from flask_restful import Api

from resources.student import Student, Students

app = Flask(__name__)
api = Api(app)

api.add_resource(Student, '/student/<int:id>')
api.add_resource(Students, '/students')

if __name__ == '__main__':
    app.run(port=7000, debug=True)