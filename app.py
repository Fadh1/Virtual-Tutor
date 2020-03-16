from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import os
import pymc3 as pm
import numpy as np
import random
import theano

app = Flask(__name__)
app.secret_key = 'some secret key'

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('welcome.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'secret' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/template')
def template():
    return render_template('first_page.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/questions')
def questions():
    return questions


@app.route('/calc')
def calc():
    num = request.args.get('num', 0, type=int)
    data1 = np.empty(0)
    numdiv = (10 - num) / 10
    for i in range(500):
        x = random.random()
        if x > numdiv:
            data1 = np.append(data1, 1)
        else:
            data1 = np.append(data1, 0)
    data = theano.shared(data1)
    with pm.Model() as model_bkt:
        a = 1
        b = 1
        theta = pm.Beta('Beta', a, b)
        p = pm.Deterministic('p', 1.0 / (1 + pm.math.exp(-1 * (theta * 10 - 5))))
        x = pm.Bernoulli('x', p=p, observed=data)
    m = pm.find_MAP(model=model_bkt)
    n = (m.get('Beta').tolist())*100
    nf = "{0:.2f}".format(n)
    return jsonify(result=nf)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
