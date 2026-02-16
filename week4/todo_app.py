from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route('/')
def show_menu():
    return '''
    <h1>To-Do App</h1>
    <ul>
        <li><a href="/tasks">View Tasks</a></li>
        <li><a href="/add?task=YourTask">Add Task</a></li>
        <li><a href="/remove?task_number=1">Remove Task</a></li>
    </ul>
    '''

@app.route('/tasks')
def view_tasks():
    return jsonify(tasks)

@app.route('/add')
def add_task():
    task = request.args.get('task')
    if task:
        tasks.append(task)
        return f"Task '{task}' added successfully!"
    return "Task cannot be empty."

@app.route('/remove')
def remove_task():
    task_number = request.args.get('task_number', type=int)
    if task_number and 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        return f"Removed task: {removed_task}"
    return "Invalid task number."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)