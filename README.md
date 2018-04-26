# Log Analysis

## Overview
This is the project for Udacity Intro to Programing Nano Degree - Back-End Development. In this project, you will use PostgresSQL to 
build an internal reporting tool that will use information from a large database to discover what kind of articles the site's readers like.
The database has the following 3 tables:

* articles - articles that has been posted so far
* authors - a list of the authors
* log - log records that sent to server (>1,000K rows)

Run the code from **main.py** you will find the answer of the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Ton Run
### What you need:
* Python 2.7
* Vagrent
* VirtualBox
* Git

### Step by step:
1. Set up VirtualBox & Vagrant
2. Clone the repository to your local computer
3. Download the news data and unzip file
4. Load the data into your local database with `psql -d news -f newsdata.sql`
5. Run the code `python main.py`
6. The output will be displayed in the bash
