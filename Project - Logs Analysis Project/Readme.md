{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue255;\red0\green0\blue0;
\red144\green1\blue18;\red0\green0\blue0;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\csgray\c0;\csgray\c100000;}
\margl1440\margr1440\vieww7380\viewh14080\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 1)This readme contains details about a Python file that upon execution connects and queries the database \'93news\'94 in postgreSQL.\
\
2)The setup that I used was a Linux Operating system having postgreSQL using Virtual Box.\
\
3)The Python file \'93pythondb.py\'94 can be run in an environment having postgresql.\
\
4)The python file - pythondb.py contains Python DB API code that upon execution queries the news database and answers the queries in the \'93Query Result Snapshot\'94 file present in the directory.\
\
5) Some of the views created in the process are:\
\
--	 
\f1 \cf2 \cb3 \expnd0\expndtw0\kerning0
create\cf4  view tvbot \cf2 as\cf4 \cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 SELECT\cf4  articles.author,articles.title, count(*) \cf2 as\cf4  views                                  \cb1 \
\cb3     \cf2 from\cf4  articles, log\cb1 \
\cb3     \cf2 WHERE\cf4  log.\cf2 path\cf4  \cf2 LIKE\cf4  \cf5 '%'\cf4  || articles.slug || \cf5 '%'\cf4  \cf2 and\cf4  log.\cf2 status\cf4 =\cf5 '200 OK'\cf4 \cb1 \
\cb3     \cf2 group by\cf4  articles.author,articles.title\cb1 \
\cb3     \cf2 order by\cf4  views \cf2 desc\cf4 ;\cb1 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0 \cf0 \kerning1\expnd0\expndtw0 \
\
This view is used to answer the 2nd Query.\
\
Execution of this view is necessary before running the pythondb.py file.\
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qc\partightenfactor0
\cf0 Description of the Program Design:\
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \'97The connection to the database news has been done with psycopg2.\
\'97There are 3 queries passed on to the variables i.e query (1,2,3).\
\'97Variables Q1,Q2,Q3 contain the query string and they are printed before each query result.\
\'97Used for loops for each query to extract the data from a particular row and a particular column.\
\
\
\
\
\

\f1\fs22 \cf6 \cb7 \CocoaLigature0 \
}