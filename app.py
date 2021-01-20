from flask import Flask, render_template, url_for, request
import helper
import os


# CONFIRMER ? voir site web install PostgreSQL
#from flask.ext.sqlalchemy import SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/orlanehouzet'
#db = SQLAlchemy(app)


# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    # get all projects from the database
    zipped = helper.get_portfolio_content()

    return render_template('/index.html',
                            id='index',
                            projects=zipped)

@app.route('/about', methods=['POST', 'GET'])
def about():
    # get all jobs from the database
    zipped = helper.get_career_content()

    return render_template('about.html',
                            career=zipped)


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    # get all projects from the database
    zipped = helper.get_portfolio_content()

    return render_template('portfolio.html',
                            projects=zipped)


@app.route('/blog', methods=['POST', 'GET'])
def blog():
    return render_template('blog.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
