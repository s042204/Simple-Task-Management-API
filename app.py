from flask import Flask
from flask_restful import Api
from models import db
from resources.task import TaskResource, TaskListResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
