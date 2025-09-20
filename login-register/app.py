import re
from flask import Flask, render_template, request
from server_module import UserNameData as und, PasswordData as pd, OtherData as od

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/authenticate', methods=['POST'])
def authenticate():
    if request.method == 'POST':
        pass
    return render_template('login.html')


@app.route('/pass_reset')
def pass_reset():
    return render_template('forgotten_password.html')


@app.route('/sign-up')
def sign_up():
    return render_template('signup.html')


body = []


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        u = und(request.form['username'],
                request.form['firstname'],
                request.form['lastname'],
                request.form['email']
                )

        p = pd(
            request.form['password'],
            request.form['confirm_password']
        )

        o = od(
            request.form['dob'],
            request.form['phone'],
            request.form['gender'],
            request.form['nationality']
        )

        u._reg(body, re)
        p._reg(body, re)
        o._reg(body, re)
    if body:
        return render_template('error.html', dymanic_content=body)
    else:
        return render_template('user_home.html')


if __name__ == '__main__':
    app.run(debug=True)
