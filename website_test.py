# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from Auth import Auth
host = "localhost"
username = "root"
password = "password"
database = "database"
# create the application object
app = Flask(__name__)
sign_up = Auth("auth_server_name", host, username, password, database)
# use decorators to link the function to a url

@app.route('/')
def home():
    return render_template('home.html')  # return a string

@app.route('/signin', methods=['GET', 'POST'])
def signin():

    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('signin.html')  # render a template

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  return render_template('signup.html', methods=['GET', 'POST'])  # render a template
 # if request.method == 'POST':
  sign_up.sign_up(firstname=request.form['firstname'], lastname=request.form['lastname'], email=request.form['email'], password=request.form['password'], confirmpassword=request.form['confirmpassword'])

#start the server with the 'run()' method
if __name__ == '__main__':
  app.run(debug=True)