from flask import Flask, jsonify, request
from utils import get_all_classes, register_to_class, register_student

app = Flask(__name__) #will take the name of the current file and use it as a name for the flask application that will deal with serving the endpoints

# getting data from the database - creating routes with @ decorator

@app.route('/classes')
def get_classes(): #get all available classes
    classes = get_all_classes()
    return jsonify(classes)

@app.route('/classes/<int:class_id>', methods=['PUT'])
def register_to_class_by_id(class_id):
    register_to_class(class_id)
#
@app.route('/students', methods=['POST'])
def register_new_student():
    #here we will need to use request- request.get_json(
    # )
    student = request.get_json()

    register_student(student['name'], student['surname'], student['email'], student['phone'], student['disability_req'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
