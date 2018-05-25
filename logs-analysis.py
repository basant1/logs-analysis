#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import psycopg2

DBNAME = "news"

# Connect to the PostgreSQL 'news' database


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def get_popular_three_articles():
    """Return the most popular three articles of all time"""
    db, c = connect()
    c.execute("select articles.title, count(*) as views "
              "from articles inner join log on log.path "
              "like concat('%', articles.slug, '%') "
              "where log.status like '%200%' group by "
              "articles.title, log.path order by views desc limit 3;")
    articles = c.fetchall()
    db.close()
    return articles


def get_popular_authors():
    """Return the most popular article authors of all time as a sorted list
    with the most popular author at the top"""
    db, c = connect()
    c.execute("select authors.name, count(*) as views from articles inner "
              "join authors on articles.author = authors.id inner join "
              "log on concat('/article/', articles.slug) = log.path where "
              "log.status like '%200%' group by authors.name order by views "
              "desc;")
    authors = c.fetchall()
    db.close()
    return authors


def get_error_date():
    """Return the day in which more than 1% of requests lead to errors"""
    db, c = connect()
    c.execute("select * from (select total.date as date, "
              "cast(error.count as FLOAT)/total.count as result "
              "from (select to_char(time,'yyyy-mm-dd') as date,count(*) "
              "as count from log group by date) as total join "
              "(select to_char(time,'yyyy-mm-dd') as date, count(*) as "
              "count from log where status='404 NOT FOUND' group by date) "
              "as error on total.date=error.date order by date DESC) as A "
              "where result>0.01 order by result desc;")
    error_date = c.fetchall()
    db.close()
    return error_date

# Generate reports


def article_report():
    article_report_result = "\n".join('''   · "%s" —- %s views''' %
                                      (title, views)
                                      for title, views in
                                      get_popular_three_articles())
    return article_report_result


def author_report():
    author_report_result = "\n".join('''   · %s —- %s views''' % (name, views)
                                     for name, views in get_popular_authors())
    return author_report_result


def error_date_report():
    error_date_report_result = "\n".join('''   · %s —- %.2f%%''' %
                                         (date, round(percent*100, 2))
                                         for date, percent in get_error_date())
    return error_date_report_result


# Merge all reports into one

REPORT = '''1. What are the most popular three articles of all time?\n%s\n\n\
2. Who are the most popular article authors of all time?\n%s\n\n\
3. On which days did more than 1%% of requests lead to errors?\n%s'''


def main():
    report = REPORT % (article_report(), author_report(), error_date_report())
    return report


if __name__ == '__main__':
    print(main())
