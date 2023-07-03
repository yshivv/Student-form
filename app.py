from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    college = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    course_name = db.Column(db.String(100), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'course' not in request.form:
            return 'Course field is required', 400

        name = request.form['name']
        college = request.form['college']
        phone = request.form['phone']
        address = request.form['address']
        course_name = request.form['course']

        try:
            student = Student(name=name, college=college, phone=phone, address=address, course_name=course_name)
            db.session.add(student)
            db.session.commit()
        except Exception as e:
            return f"An error occurred: {str(e)}", 500

    students = Student.query.all()
    return render_template('index.html', students=students)


if __name__ == '__main__':
    db.create_all()
    app.run()

migrate = Migrate(app, db)
