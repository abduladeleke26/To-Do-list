from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

to_do = []

def numbering(list):
    for item in list:
        num = list.index(item)
        item["id"] = num + 1


@app.route('/')
def home():
    todo = to_do
    return render_template("index.html", todo = todo)

@app.route('/add', methods=['POST'])
def add():
    new_task = {"id": (len(to_do)+1), "obj": request.form.get('task'), "completed": False}
    to_do.append(new_task)
    todo = to_do
    return render_template("index.html", todo = todo)

@app.route('/done', methods=['POST'])
def buttons():
    complete = request.form.get('complete')
    delete = str(request.form.get('delete'))

    for task in to_do:
        if complete == str(task['id']):
            if task["completed"] == True:
                task["completed"] = False
            else:
                task["completed"] = True
        if delete == str(task['id']):
            to_do.remove(task)
            numbering(to_do)


    todo = to_do
    return render_template("index.html", todo = todo)







if __name__ == "__main__":
    app.run(debug=True)
