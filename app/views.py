from flask import render_template, jsonify
from app import app
from app.models import User, List, Task

# Todo Views
@app.route('/')
@app.route('/todo')
def index():
    return render_template('index.html', name='YOUR NAME HERE')

@app.route('/todo/login')
# Example URL: http://www.todo.com
def login():
    # let's see if we can implement a login page
    # http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
    pass

@app.route('/todo/<int:user_id>/logout')
# Example URL: http://www.todo.com/1
def logout():
    # we will worry about authentication later
    pass

@app.route('/todo/<int:user_id>/task/<new_task>', methods=['POST'])
# Example URL: http://www.todo.com/1/task/1
def create_task(new_task):
    Task.objects.create(new_task)

@app.route('/todo/<int:user_id>/task/<int:task_id>', methods=['GET'])
# Example URL: http://www.todo.com/1/task/1
def get_task(user_id, task_id):
    task = Task.objects.filter(id=task_id)
    if (task.list__owner != user_id):
        abort(404)
    else:
        return jsonify(task)

@app.route('/todo/<int:user_id>/tasks', methods=['GET'])
# Example URL: http://www.todo.com/1/tasks
def get_tasks(user_id):
    tasks = Task.objects.filter(list__owner=user_id)
    return jsonify({'tasks': tasks})