# -*- coding: utf-8 -*-


from flask import request, render_template, flash, abort, url_for, redirect, session

from blog import app
from blog.model.user import User
from blog.model.article import Article


@app.route('/')
def show_articles():
    articles = []
    total, titles, contents = Article.total(), Article.fields(), Article.values()
    
    for i in xrange(0, total):
        articles.append({
            'title': titles[i].decode('utf-8'), 
            'content': contents[i].decode('utf-8')
        })

    return render_template('show_articles.html', articles=articles)


@app.route('/add_article', methods=['POST'])
def add_article():
    if not session.get('logged_in'):
        abort(401)

    Article(request.form['title'], request.form['text'])
    flash('Success post new article: %s !' % request.form['title'])

    return redirect(url_for('show_articles'))


@app.route('/login', methods=['GET','POST'])
def login():
    error = None

    if request.method == 'POST':
        if not User.exist(request.form['username']):
            error = 'Invalid Username !'

        elif User.get(request.form['username']) != request.form['password']:
            error = 'Error Password !'

        else:
            session['logged_in'] = True
            flash('Success Login !')
            return redirect(url_for('show_articles'))

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Success Logout !')
    return redirect(url_for('show_articles'))
