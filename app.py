from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# On stocke les tâches dans une liste (en mémoire)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_text = request.form.get('task')
        if task_text:
            tasks.append({'text': task_text, 'done': False})
        return redirect(url_for('index'))
    
    return render_template('index.html', tasks=tasks)

@app.route('/toggle/<int:index>')
def toggle(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = not tasks[index]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)