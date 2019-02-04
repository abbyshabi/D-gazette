from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_sources, get_articles
from ..models import Sources,Articles


@main.route('/')
def index():
    """
    View root page function that returns index page and the various news sources
    """
    title = 'Home- Welcome to the best News source page'
 
    news_sources = get_sources('sources')
    return render_template('index.html', title=title, news_sources=news_sources,id = id)


@main.route('/articles/<id>')
def article(id):
    '''
    The view page for the news page
    '''
    article = get_articles(id)
    return render_template('articles.html', article = article, id = id)

@main.route("/sources/<category>")
def sources(category):
    """
    View function for the source pages
    """
    sources = get_sources(category)
    title = category.capitalize()
    header = category.capitalize()
    return render_template("sources.html",sources = sources,title = title,header = header)