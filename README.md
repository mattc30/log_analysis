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
2. Download or clone the [FSND-VM](https://github.com/udacity/fullstack-nanodegree-vm) repository
3. Download [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
4. Unzip the file, move newsdata.sql into vagrant folder
5. Load the data into your local database with `psql -d news -f newsdata.sql`
6. Connect to your database using `psql -d news`, then you can explore the tables
7. Run the code `python main.py`
8. The output will be displayed in the bash

### Launching virtual machine:
1. Go into the downloaded fullstack-nanodegree-vm repository enter command:
```
  $ vagrant up
```
2. Log in using command:
```
  $ vagrant ssh
```
3. Change directory to vagrant using command:
```
  $ cd /vagrant
```
