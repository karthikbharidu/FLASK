from flask import Flask,render_template,flash,redirect,url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'vivitha'

Regsiter_details = []

    
@app.route('/')
def flask():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/register' , methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account Created')
        return redirect(url_for('login'))
    if form.errors:
        flash('validation errors:' +str(form.errors))
        app.logger.error('validationError:\n'+ str(form.errors))
    return render_template('register.html', title = "register", form = form)

@app.route("/Login",methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'karthikvsnani@gmail.com' and form.password.data  == '1234':
            flash('logged in')
            return redirect(url_for('home'))
    return render_template('login.html', title = 'Login', form = form)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



if __name__ == "__main__":    
    app.run(debug = True)
