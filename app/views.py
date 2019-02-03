from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources, get_source_articles
from .model import source
from .model import articles
import requests
import json


Articles= articles.Articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Home - Welcome to D-Gazette"
    news_sources = get_sources('sources')
    return render_template('index.html',title = title,news_sources = news_sources)