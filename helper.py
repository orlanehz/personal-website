from flask import request
import psycopg2
import os

def get_portfolio_content():
    '''
    Function to get the portfolio projects from the database
    Returns: zipped
    '''


    # connect to database
    DATABASE_URL = "postgres://kanyaexqxpdlad:bcfd85a8e3194ebd90745f8bc318618774a75541f0825d696d32cb13f07ee85c@ec2-52-205-145-201.compute-1.amazonaws.com:5432/d23t5b583puabs"
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    # select rows from the database
    cur.execute("SELECT * FROM portfolio")
    db_row = cur.fetchall()
    # close database connection
    conn.close()


    # instantiate a list to save all projects in
    project_list = []
    # iterate through all the projects in the database
    for project in db_row:
        one_project = []
        # add the title, description, skills and image name
        one_project.extend(project[1:])
        # instantiate list for links
        #links = []
        #if project[6] != 'NaN':
         #   links.append(["Blog Post", project[6]])
        #if project[5] != 'NaN':
         #   links.append(["Code", project[5]])
        #one_project.append(links)

        # assign single project to entire project_list
        project_list.append(one_project)

    # create list of lists that contains pairs of projects
    #if len(project_list) % 2 == 0:
     #   pass
    #else:
        project_list.append(['placeholder'])
    iterator = iter(project_list)
    zipped = zip(iterator, iterator)

    return zipped