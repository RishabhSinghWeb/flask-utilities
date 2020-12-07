from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	complete = db.Column(db.Boolean)


@app.route("/")
def home():
	return render_template("base.html", todo_list=Todo.query.all(),aaaa="aaa")


@app.route("/add", methods=["POST"])
def add():
	passw=request.form.get("pass")
	if passw:
		db.session.add(Todo(title=passw, complete=False))
		db.session.commit()
	return redirect(url_for("home"))

@app.route("/<int:todo_id>")
def update(todo_id):
	todo = Todo.query.filter_by(id=todo_id).first()
	todo.complete = not todo.complete
	db.session.commit()
	return redirect(url_for("home"))


@app.route("/<int:todo_id>/del")
def delete(todo_id):
	db.session.delete(Todo.query.filter_by(id=todo_id).first())
	db.session.commit()
	return redirect(url_for("home"))


@app.route("/a")
def a():
	return render_template("a.html")

@app.route("/aa", methods=["POST"])
def aa():
	return "hi"

if __name__ == "__main__":
	with open('./log', 'a+') as log:
		try:
			db.create_all()
			app.run(host="0.0.0.0",port=80, threaded=True, debug=False)
			log.write("done adding wsgi app\n")
		except Exception:
			log.write(repr(e))
