import sqlite3

from flask_restful import Resource, reqparse


class Student(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('id',                        required='True',                        help='ID is mandatory!')
    parser.add_argument('firstName',
                        required=True,
                        help="FNAME Require!"
                        )

    parser.add_argument('lastName')
    parser.add_argument('stuAddress')
    parser.add_argument('stuClass')

    # id int UNIQUE, first_name text, last_name text, Class text, Address text

    @classmethod
    def student_by_id(cls, id):
        connection = sqlite3.connect('resources\school.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM students WHERE id=?"
        results = cursor.execute(select_query, (id,))
        row = results.fetchone()
        connection.close()

        if row:
            return {
                'student': {'id': row[0], 'firstName': row[1], 'lastName': row[2], 'class': row[3], 'address': row[4]}}

    @classmethod
    def studentinsert(cls, id, data):
        connection = sqlite3.connect('resources\school.db')
        cursor = connection.cursor()

        query = 'INSERT INTO students VALUES (?, ?, ?, ?, ?)'
        cursor.execute(query, (id, data['firstName'], data['lastName'], data['stuAddress'], data['stuClass']))

        connection.commit()
        connection.close()

    def get(self, id):
        student = self.student_by_id(id)
        if student:
            return student
        return {'message': 'Student not found'}, 404

    def post(self, id):
        if self.student_by_id(id):
            return {'message': f'Existing student with same id:{id}'}, 400

        data = Student.parser.parse_args()
        student = {'student': {'id': id, 'firstName': data['firstName'], 'lastName': data['lastName'],
                               'class': data['stuAddress'], 'address': data['stuClass']}}
        print(student)
        self.studentinsert(id, data)

        return student, 201

    def put(self, id):
        student = self.student_by_id(id)

        data = Student.parser.parse_args()
        student_item = {'student': {'id': id, 'firstName': data['firstName'], 'lastName': data['lastName'],
                                    'class': data['stuAddress'], 'address': data['stuClass']}}
        returnCode = 0

        if student is None:
            try:
                self.studentinsert(id, data)
                returnCode = 201
            except:
                return {"message": "Error occured in data insert"}, 500
        else:
            try:
                connection = sqlite3.connect('resources\school.db')
                cursor = connection.cursor()
                update_query = 'UPDATE students SET first_name=?,  last_name=?, Class=?, Address=? WHERE id=?'
                cursor.execute(update_query, (data['firstName'], data['lastName'], data['stuClass'], data['stuAddress'], id))
                connection.commit()
                connection.close()
                returnCode = 200
            except:
                return {"message": "Error occured in data update as student existed"}, 500

        return student_item, returnCode

class Students(Resource):
    def get(self):
        connection = sqlite3.connect('resources\school.db')
        cursor = connection.cursor()

        select_query = 'SELECT * FROM students'
        tempresults = cursor.execute(select_query)
        print(len(tempresults.fetchall()))
        results = cursor.execute(select_query)
        students = []
        for row in results:
            students.append({'id': row[0], 'firstName': row[1], 'lastName': row[2], 'class': row[3], 'address': row[4]})

        connection.close()
        return {'students': students}
