# Log_Analysis
This is a project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Project Description:
Create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program 
using the psycopg2 module to connect to the database.

### What needs to be achieved?
1. **What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

**_Example_**:

+ Princess Shellfish Marries Prince Handsome — 1201 views
+ Baltimore Ravens Defeat Rhode Island Shoggoths — 915 views
+ Political Scandal Ends In Political Scandal — 553 views

2. **Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

**_Example_**:

+ Ursula La Multa — 2304 views
+ Rudolf von Treppenwitz — 1985 views
+ Markoff Chaney — 1723 views
+ Anonymous Contributor — 1023 views 

3. **On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

**_Example_**:

July 29, 2016 — 2.5% errors

## Requirements
* Python 3.5.3
* psycopg2
* Postgresql 9.6

+ **Setup required** - [Setup](Setup.md) 

## How to run?

* Load the data using the following command: 
```sql
psql -d news -f newsdata.sql 
```
* Connect to the database
```sql
psql -d news
```
+ **Create views** - [Views](View.md)

1. You should already have vagrant up and be connected to it. 
1. If you aren't already, cd into the correct project directory: ``` cd /vagrant/log_analysis ```
1. Run ``` python3 LogAnalysis.py ```

Generating this information will take several seconds, but will now start loading. 

+ [**Project Output**](Output.txt)

### Contributors
Udacity

### License

Licensed under [MIT license](LICENSE)
