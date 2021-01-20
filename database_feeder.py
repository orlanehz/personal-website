import pandas as pd 
import numpy as np
import psycopg2
import os


# read in all necessary Excel files
portfolio_df = pd.read_excel("database/portfolio_db.xlsx")
career_df = pd.read_excel("database/career_db.xlsx")

# connect and create tables if they don't exist yet
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()



cur.execute("DROP TABLE portfolio")
cur.execute("CREATE TABLE IF NOT EXISTS portfolio \
            (id SERIAL, title text NOT NULL, description text, skills text, \
             image text, code text, blog_post text, maj_date text, tag text, alt text)")

# select everything from the portfolio database
cur.execute("TRUNCATE portfolio RESTART IDENTITY")


# read the data into the portfolio database
# iterate through the dataframe generated from the Excel file
for portfolio_row in portfolio_df.itertuples():
    cur.execute("INSERT INTO portfolio (title, description, skills, image, code, blog_post, maj_date, tag, alt) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                [portfolio_row.title, portfolio_row.description,
                 portfolio_row.skills, portfolio_row.image, portfolio_row.code,
                 portfolio_row.blog_post, portfolio_row.maj_date, portfolio_row.tag, portfolio_row.alt])
    conn.commit()




cur.execute("DROP TABLE career")
cur.execute("CREATE TABLE IF NOT EXISTS career \
            (id SERIAL, title text NOT NULL, image text, value_added text, \
             culture_fit text, conclusion text, company text, period text, alt text)")

# select everything from the career database
cur.execute("TRUNCATE career RESTART IDENTITY")


# read the data into the career database
# iterate through the dataframe generated from the Excel file
for career_row in career_df.itertuples():
    cur.execute("INSERT INTO career (title, image, value_added, culture_fit, conclusion, company, period, alt) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                [career_row.title, career_row.image,
                 career_row.value_added, career_row.culture_fit, career_row.conclusion,
                 career_row.company, career_row.period, career_row.alt])
    conn.commit()


conn.close()