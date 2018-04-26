import psycopg2

def run_query(query):
    """connects the database, runs the query pass to it,
    returns the result"""
    db=psycopg2.connect('dbname=news')
    c=db.cursor()
    c.execute(query)
    result=c.fetchall()
    db.close()
    return result


def top_three_articles():
    """this function get 3 most read articles"""
    query1="""
        SELECT articles.title, COUNT (*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3
    """

    # run the query and get the result
    results=run_query(query1)

    # print out the result
    print ('\nThe most popular three articles of all time:')
    for i in results:
        title=i[0]
        view=str(i[1])
        print ('\t' + title + ' - ' + view + ' views')


def most_popular_authors():
    """this function get the most popular authors"""
    query2="""
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
    results=run_query(query2)

    # print out the result
    print ('\nMost popular article authors of all time:')
    for i in results:
        title=i[0]
        view=str(i[1])
        print('\t' + title + ' - ' + view + ' views')


def most_errors_date():
    """
    this function get the dates with more than 1 percent
    of requests lead to errors
    """
    query3="""
        SELECT errors.day,
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
    results=run_query(query3)

    # print out the result
    print ('\nDays with more than 1% of' 
            ' errors:')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(i[1]) + '%' + ' errors'
        print ('\t' + date + ' - ' + errors)


top_three_articles()
most_popular_authors()
most_errors_date()