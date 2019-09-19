from flask import Flask, jsonify
app = Flask(__name__)

instructors = [
    { 'firstName': "Muhammad Ali", 'lastName': "Kahoot"  },
    { 'firstName': "Umer", 'lastName': "Munir"  },
    { 'firstName': "Muhammad", 'lastName': "Hammad"  }
]

students = [
    {'firstName':"Habib Ur Rehman", 'lastName':"Malik"},
    {'firstName':"Nausherwan",'lastName':"Khan"},
    {'firstName':"Hashir",'lastName':"Khan"}
]

@app.route('/hello')
def hello():
    greeting = "Hello User Sir!"
    return greeting

@app.route('/welcome')
def welcome():
    greeting = "Welcome to the world of Kubernetes and Jenkins :)"
    return greeting

@app.route('/instructors', methods=["GET"])
def getInstructors():
    return jsonify(instructors)

@app.route('/instructor/<id>', methods=["GET"])
def getInstructor(id):
    id = int(id) - 1
    return jsonify(instructors[id])

@app.route('/student/<id>', methods=["GET"])
def getStudent(id):
    id = int(id) - 1
    return jsonify(students[id])

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)