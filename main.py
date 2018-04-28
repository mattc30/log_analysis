#!/usr/bin/env python
import psycopg2

question1 = '\nWhat are the most popular three articles of all time?'
question2 = '\nWho are the most popular article authors of all time?'
question3 = ('\nOn which days did more than 1% of requests lead \
to errors?')


def connect(database_name='news'):
    """connect to database and return a connection"""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except Exception:
        print("Oops! Fail to connect to database!")


def run_query(query):
    """
    runs the query pass to it, returns the result
    """
    db, cursor = connect()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def print_results(ques, results, word):
    print ques
    for i in results:
        print ('\t' + str(i[0]) + ' - ' + str(i[1]) + word)


def top_three_articles():
    """this function get 3 most read articles"""
    query1 = """
        SELECT articles.title, COUNT (*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3
    """

    # run the query and get the result
    results = run_query(query1)

    # print out the result
    print_results(question1, results, ' views')


def most_popular_authors():
    """this function get the most popular authors"""
    query2 = """
        SELECT authors.name, COUNT (*) AS num
        FROM authors
        JOIN articles
        ON authors.id=articles.author
        JOIN log
        ON log.path LIKE concat('/article/', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
    """

    # run the query and get the result
    results = run_query(query2)

    # print out the result
    print_results(question2, results, ' views')


def most_errors_date():
    """
    this function get the dates with more than 1 percent
    of requests lead to errors
    """
    query3 = """
        SELECT to_char(errors.day, 'Mon DD, YYYY'),
            round(((errors.error_requests*1.0)/total.requests)*100, 2)\
            AS percent
        FROM (
            SELECT date_trunc('day', time) AS "day", \
            COUNT (*) AS error_requests
            FROM log
            WHERE status LIKE '404%'
            GROUP BY day
        ) AS errors
        JOIN (
            SELECT date_trunc('day', time) AS "day", \
            COUNT (*) AS requests
            FROM log
            GROUP BY day
        ) AS total
        ON errors.day = total.day
        WHERE (round(((errors.error_requests*1.0)/total.requests)*100,\
         1) > 1)
    """

    # run the query and get the result
    results = run_query(query3)

    # print out the result
    print_results(question3, results, '% errors')


top_three_articles()
most_popular_authors()
most_errors_date()
