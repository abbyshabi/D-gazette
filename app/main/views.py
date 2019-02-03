from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Sources
from ..models import Articles
import json


#Articles= article.Articles

# Views
@main.route('/')
def index():

    '''
    The root view for the index page
    '''
    title = "Home - Welcome to D-Gazette"
    news_sources = get_sources('sources')
    return render_template('index.html',title = title,news_sources = news_sources)

@main.route('/news/<source_id>')
def news(source_id):
    '''
    The view page for the news page
    '''
    news_args = get_articles(id)
    return render_template('news.html', news=news_args)
