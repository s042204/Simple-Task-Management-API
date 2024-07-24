from flask_restful import Resource, reqparse
from models import Task, db

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='Title cannot be blank!')
parser.add_argument('description', type=str)
parser.add_argument('done', type=bool)

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        }

    def put(self, task_id):
        data = parser.parse_args()
        task = Task.query.get_or_404(task_id)
        task.title = data['title']
        task.description = data['description']
        task.done = data['done']
        db.session.commit()
        return {'message': 'Task updated'}

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return {'message': 'Task deleted'}

class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return [{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        } for task in tasks]

    def post(self):
        data = parser.parse_args()
        new_task = Task(
            title=data['title'],
            description=data.get('description', ''),
            done=data.get('done', False)
        )
        db.session.add(new_task)
        db.session.commit()
        return {'message': 'Task created'}, 201
