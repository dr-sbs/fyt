from flask import Flask, render_template, redirect, url_for, jsonify, request, flash
from forms import RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Guptaji the great'





@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/a/login', methods=['GET', 'POST'])
def admin_login():
    ''' Route for admin login '''
    if request.method == "POST":
        # replace with WTF forms later on
        login_id = request.form.get('login-id', '')
        login_password = request.form.get('login-password', '')
        print(login_id, login_password)
        return redirect(url_for('admin_login'))
    return render_template('admin-login.html')


@app.route('/login')
def login():
    ''' Route for tutor/student login '''
    if request.method == "POST":
        # replace with WTF forms later on
        login_id = request.form.get('login-id', '')
        login_password = request.form.get('login-password', '')
        print(login_id, login_password)
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def user_register():
    form = RegistrationForm() 
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Your account was created', 'success')
            return redirect(url_for('login'))
        else:
            return render_template('register.html',form=form)
    else:
        return render_template('register.html',form=form)

@app.errorhandler(404)
def error_handler(e):
    ''' For Handling 404 error '''
    return render_template('404.html')


if __name__=='__main__':
    app.run(debug=True)