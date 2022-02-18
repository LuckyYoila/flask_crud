from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

todoData = []

@app.route("/")
def indexs():
    return render_template("index.html", todos = todoData)

@app.route('/create_todo', methods=["POST"])
def create_todo():
    new_todo = request.form.get("new_todo")
    todoData.append(new_todo)
    print(todoData)
    return redirect(url_for("indexs"))

@app.route('/delete/<todo_item>') 
def delete(todo_item):
    todoData.remove(todo_item)

    return redirect(url_for('indexs'))

if __name__ == "__main__":
    app.run(debug=True)
