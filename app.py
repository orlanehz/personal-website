from flask import Flask, render_template, url_for

from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/orlanehouzet'
db = SQLAlchemy(app)





# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('/index.html',
                            id='index')

@app.route('/about', methods=['POST', 'GET'])
def about():

    # default language if just portfolio is entered in url
    lang = 'en'

    return render_template('about.html')





@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    # default language if just portfolio is entered in url
    lang = 'en'

    return render_template('portfolio.html')


@app.route('/blog', methods=['POST', 'GET'])
def blog():

    # default language if just portfolio is entered in url
    lang = 'en'

    return render_template('blog.html',
                            lang=lang)

@app.route('/contact', methods=['POST', 'GET'])
def contact():

    # default language if just portfolio is entered in url
    lang = 'en'

    return render_template('contact.html',
    						lang=lang)
