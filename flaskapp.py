# flaskapp.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data store, replace with a database in a real application
user_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        # Store data in the dictionary (replace with a database in a real application)
        user_data[username] = {
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }

        return redirect(url_for('display_info', username=username))

    return render_template('register.html')

@app.route('/display/<username>')
def display_info(username):
    user_info = user_data.get(username, None)
    return render_template('display.html', user_info=user_info)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username and password match (authentication logic)
        if username in user_data and user_data[username]['password'] == password:
            return redirect(url_for('display_info', username=username))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
