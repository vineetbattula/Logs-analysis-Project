#!/usr/bin/env python

import psycopg2
import datetime

DBNAME = "news"


"""Return all queries from the 'database'"""
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
query1 = """SELECT articles.title, count(*) as views
    from articles, log
    WHERE log.path LIKE '%' || articles.slug || '%' and log.status='200 OK'
    group by articles.title
    order by views desc
    limit 3;"""
c.execute(query1)
results = c.fetchall()

Q1 = """1. What are the most popular three articles of all time?"""
print Q1
for row in results:
    print row[0] + " -- " + str(row[1]) + " views"

query2 = """select authors.name, authors.id, sum(tvbot.views) as total_views
from
tvbot, authors
where authors.id= tvbot.author
group by authors.name, authors.id
order by total_views desc;"""

c.execute(query2)
results = c.fetchall()

Q2 = """2. Who are the most popular article authors of all time?"""
print Q2
for row in results:
    print row[0] + " -- " + str(row[2]) + " views"

query3 = """select A.date as Date, (B.count/A.count::float *100)
as ERROR_PERCENTAGE from
(select date(log.time), count(*)
from log group by date) as A join(select date(log.time), log.status ,
count(*) from log
where log.status = '404 NOT FOUND'
group by date,log.status
order by date) as B On A.date = B.date where (B.count/A.count::float *100)> 1;
"""
c.execute(query3)
results = c.fetchall()


Q3 = """3. On which days did more than 1% of requests lead to errors? """
print Q3

for row in results:
    print str(row[0]) + " -- " + str(row[1]) + "% errors"
