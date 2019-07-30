from flask import render_template

from app import app


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
