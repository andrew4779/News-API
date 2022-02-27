from xml.etree.ElementTree import Comment
from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_news_sources, get_news_articles

#Views
@main.route('/')
def index():
  '''
  View root page that returns the index page and its data
  '''
  # uncomment line 13
  # sources = get_news_sources('sources')
  title = 'Home - Welcome to The best News Website Online'
  # Comment sources/deleted (sources = sources)try add see if works later)
  return render_template('index.html', title = title,)


@main.route('/articles')
def articles():
  articles = get_news_articles()
  title = 'Home - Welcome to The best News Website Online'
  return render_template('articles.html', title = title, articles = articles)