
from flask import render_template
import feedparser

from flask import Flask
app = Flask(__name__)

RSS_FEEDS= {'cnn':'http://rss.cnn.com/rss/edition.rss',
            'bbc': 'http://feeds.bbci.co.uk/news/world/rss.xml',
            'fox':'http://feeds.foxnews.com/foxnews/latest',
            'iol':'http://rss.iol.io/rn/news'}




@app.route("/")
@app.route("/<publication>")
def get_news(publication='bbc'):
    feed=feedparser.parse (RSS_FEEDS[publication])
    first_article = feed ['entries'][0]
    return render_template ("home.html",articles=feed['entries'])







if __name__ == '__main__':
    app.run(port=5000, debug=True)