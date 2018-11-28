

#  Log Analysis Project  
#### This is Udacity first project for full stack web development nano-degree (2018)
## About This Project:
###### This project, is a good practice for your SQL database skills by interacting with a live Database that contain millions of rows, then build and refine complex queries and use them to draw business conclusions from data.
##  How To Start The Project:
### you will need.
 -  Python 
 - Install virtual Box  [Download virtual Box](https://www.virtualbox.org/wiki/Downloads)
 - Install vagrant [Download vagrant](https://www.vagrantup.com/downloads.html)
 - Download fullstack-nanodegree-vm and Unzip it
 - Download newsdata.sql and Unzip it 
 - Run your (VM)
 - Lode data Using `psql -d news -f newsdata.sql`
## Project Request
### What to report ?
 - What are the most popular three articles of all time?

	Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top. 

 - Who are the most popular article authors of all time?
 
	That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

 - On which days did more than 1% of requests lead to errors?
 
	 The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 

## Run This Project 
### to report the first and second request 
#### create view mylog 

       create view mylog as 
       (select count ( substr(path,10)) as counet, 
       substr(path,10) as newpath
       from log GROUP BY path ORDER BY newpath);

#### Then follow the steps in newsDBsolution.py     
### to report the third  request  
#### create create view ok 

    create view ok AS (select DATE(time),
      COUNT(status) from log where status = '200 OK' 
      GROUP BY DATE(time)); 
#### create create view notok 

    create  view notok AS (select DATE(time),  
    COUNT(status) from log where status NOT LIKE  '200 OK' 
    GROUP BY DATE(time));
#### create create view allnewstatus

    create view allnewstatus 
    AS select ok.date AS alldate, notok.count 
    AS errCunt, ok.count AS truCunt from ok 
    JOIN notok ON (ok.date = notok.date);
#### Then follow the steps in newsDBsolution.py      

 




