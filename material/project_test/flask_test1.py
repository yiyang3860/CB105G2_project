from flask import Flask, render_template, redirect, request, url_for, flash
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)

# @app.route('/para/<user>')
# def index(user):
#     return render_template('abc.html', user_template=user)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return 'Hello ' + request.values['username']
#
#     return "<form method='post' action='/login'><input type='text' name='username' />" \
#             "</br>" \
#            "<button type='submit'>Submit</button></form>"

@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if login_check(request.form['username'], request.form['password']):
            flash('Login Success!')
            return redirect(url_for('hello', username=request.form.get('username')))
    return render_template('login.html')

def login_check(username, password):
    """登入帳號密碼檢核"""
    if username == 'admin' and password == 'hello':
        return True
    else:
        return False

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "Your Key"
    app.run()