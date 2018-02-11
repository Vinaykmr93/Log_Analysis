#! / usr/bin/env python3
import psycopg2


DBNAME = 'news'


def connect(database_name=DBNAME):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        return db, c
    except:
        print("Connection to Database failed")


# First Query
def first_query():
    db, c = connect()

    popular_articles = """
    select article_title, count(*) as total_reads from article_info
    group by article_title order by total_reads desc limit 3;
    """

    c.execute(popular_articles)
    print("\n")
    print("Most popular article of all time:\n")
    for (article_title, total_reads) in c.fetchall():
        print("    {} - {} views".format(article_title, total_reads))
    print("\n")
    print("*"*70)
    c.close()
    db.close()


# Second Query
def second_query():
    db, c = connect()
    popular_authors = """
    select article_id, name as author_name, count(*) as author_reads
    from article_info, authors
    where article_info.article_id = authors.id
    group by article_id, author_name order by author_reads desc;
    """
    c.execute(popular_authors)
    print("Most popular authors:\n")
    for(article_id, author_name, author_reads) in c.fetchall():
        print("    {} - {} - {} views".format(article_id, author_name,
              author_reads))
    print("\n")
    print("*"*70)
    c.close()
    db.close()


# Third Question
def third_query():
    db, c = connect()
    error_calculation = """
    select date, error_percentage from log_calc where error_percentage > 1;
    """

    c.execute(error_calculation)
    print("Days with more than 1% error:\n")
    for(date, error_percentage) in c.fetchall():
        print("  {} - {} views\n".format(date, error_percentage))
    print("*"*70)

    c.close()  # Close cursor
    db.close()  # Close Database

first_query()
second_query()
third_query()
