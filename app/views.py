from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources
from .models import source
from .models import article

import json


Articles= article.Articles

# Views
@app.route('/')
def index():

    '''
    The root view for the index page
    '''
    title = "Home - Welcome to D-Gazette"
    news_sources = get_sources('sources')
    return render_template('index.html',title = title,news_sources = news_sources)

@app.route('/article/<source_id>')
def source(source_id):
    '''
    The view page for the news page
    '''

    
    source_and_articles = get_source_articles(source_id)
    return render_template('news.html', source_and_articles=source_and_articles)
