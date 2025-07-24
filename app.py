from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/smart_project"
app.config['SQLALCHEMY_TEACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Create, Update, Search, Delete

@app.route("/")
def landingPage():
    return render_template('landing-page.html')
@app.route("/classes1")
def classes1():
    return render_template('classes1.html')
@app.route("/classes2")
def classes2():
    return render_template('classes2.html')
@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/sign-up", methods=["GET"])
def signUp():
    return render_template('sign-up.html')

@app.route("/sign-up", methods=["POST"])
def createUser():
    # get request params
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")

    # save these params to db
    user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    
    res = {}

    res["code"] = 200
    res["message"] = f"User added successfully"

    return jsonify(res)

@app.route("/parent")
def parent():
    return render_template('parent.html')
@app.route("/student")
def student():
    return render_template('student.html')
@app.route("/teacher")
def teacher():
    return render_template('teacher.html')
@app.route("/classes")
def classes():
    return render_template('classes.html')
@app.route("/assignments")
def assignments():
    return render_template('assignments.html')
@app.route("/school")
def school():
    return render_template('school.html')
@app.route("/reports")
def reports():
    return render_template('reports.html')
@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/tell-us-about-yourself")
def tellUsAboutYourself():
    return render_template('tell-us-about-yourself.html')
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')
@app.route("/add-courses")
def addCourses():
    return render_template('add-courses.html')
@app.route("/add-courses-age-group")
def addCoursesAgeGroup():
    return render_template('add-courses-age-group.html')
@app.route("/add-courses-type")
def addCoursesType():
    return render_template('add-courses-type.html')
@app.route("/add-courses-subject")
def addCoursesSubject():
    return render_template('add-courses-subject.html')
@app.route("/add-courses-free")
def addCoursesFree():
    return render_template('add-courses-free.html')
@app.route("/add-courses-free-premium")
def addCoursesFreePremium():
    return render_template('add-courses-free-premium.html')
@app.route("/add-courses-exam-board")
def addCoursesExamBoard():
    return render_template('add-courses-exam-board.html')


@app.route("/students")
def students():
    return render_template('student.html')

@app.route("/teachers")
def teachers():
    return render_template('teacher.html')

@app.route("/course-Math")
def courseMath():
    return render_template('course-mathematics-dasboard.html')













    
    
@app.route("/help")
def help():
    return render_template('help.html')
@app.route("/resource")
def resource():
    return render_template('resource-search.html')
@app.route("/region")
def region():
    return render_template('region.html')

@app.route("/notifications")
def notifications():
    return render_template('notifications.html')
@app.route("/acc_settings")
def acc_settings():
    return render_template('account-setting.html')
@app.route("/reports1")
def reports1():
    return render_template('reports3.html')

if __name__ == '__main__':
    app.run(debug=True)

