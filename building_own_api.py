from flask import Flask, jsonify, request
from pprint import pprint
# from utils import

app = Flask(__name__) #will take the name of the current file and use it as a name for the flask application that will deal with serving the endpoints

# getting data from the database - creating routes with @ decorator
@app.route('/')
def welcome():
    return {'hello': 'welcome to CFGDrums!'}

@app.route('/classes')
def get_classes(): #get all available classes
    return # jsonify(classes)

@app.route('/classes/<int:class_id>')
def get_class_by_id(class_id):
    return #

@app.route('/students', methods=['POST'])
def register_student():
    #here we will need to use request- request.get_json(
    # )
    return ' '




if __name__ == '__main__':
    app.run(debug=True)