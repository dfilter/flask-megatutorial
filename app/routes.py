from flask import flash, redirect, render_template, url_for

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = dict(username='dfilter')
    posts = [
        dict(author=dict(username='John'), 
             body='Beautiful day in Burlington!'),
        dict(author=dict(username='Susan'), 
             body='When is John comming back?!')]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
