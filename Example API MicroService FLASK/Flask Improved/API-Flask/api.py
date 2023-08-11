from flask import Flask, jsonify, request

app = Flask(__name__)

# sample data
students = [
    {'id': 1, 'name': 'John', 'age': 20},
    {'id': 2, 'name': 'Jane', 'age': 21},
    {'id': 3, 'name': 'Bob', 'age': 22}
]

# endpoint to retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# endpoint to retrieve a specific student
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = [student for student in students if student['id'] == id]
    if len(student) == 0:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(student[0])

# endpoint to create a new student
@app.route('/students', methods=['POST'])
def create_student():
    student = {
        'id': request.json['id'],
        'name': request.json['name'],
        'age': request.json['age']
    }
    students.append(student)
    return jsonify(student), 201

# endpoint to update a student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = [student for student in students if student['id'] == id]
    if len(student) == 0:
        return jsonify({'error': 'Student not found'}), 404
    student[0]['name'] = request.json.get('name', student[0]['name'])
    student[0]['age'] = request.json.get('age', student[0]['age'])
    return jsonify(student[0])

# endpoint to delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = [student for student in students if student['id'] == id]
    if len(student) == 0:
        return jsonify({'error': 'Student not found'}), 404
    students.remove(student[0])
    return jsonify({'message': 'Student deleted'})

if __name__ == '__main__':
    app.run(debug=True)
