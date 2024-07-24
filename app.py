from flask import Flask, request, jsonify
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return "Welcome to the Task Management API!"

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data.get('description', ''))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created successfully!"}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    output = []
    for task in tasks:
        task_data = {'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done}
        output.append(task_data)
    return jsonify({"tasks": output})

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    task_data = {'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done}
    return jsonify(task_data)

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    task.title = data['title']
    task.description = data.get('description', task.description)
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify({"message": "Task updated successfully!"})

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
