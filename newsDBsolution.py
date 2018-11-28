# The created view are in README.md file This
import psycopg2
DBName = "news"
request1 = ("What are the most popular three articles of all time? ")
Query1 = ('''select articles.title , mylog.counet from articles LEFT JOIN mylog ON (CAST(articles.slug AS TEXT) LIKE CAST(mylog.newpath AS TEXT)) ORDER BY mylog.counet desc limit 3 ; ''')
request2 = ("Who are the most popular article authors of all time ?")
Query2 = ('''select authors.name, SUM(mylog.counet) AS Viewer from articles JOIN mylog ON (articles.slug = mylog.newpath) JOIN authors ON (authors.id = articles.author) GROUP BY authors.name ORDER BY Viewer DESC limit 3; ''')
request3 =("the days that lead to more than 1% of requests errors !?")
Query3 = ('''select  alldate, (100 - (((trucunt-errcunt) / trucunt::float) * 100)) AS perc from allnewstatus GROUP BY alldate,perc HAVING (100 - (((trucunt-errcunt) / trucunt::float) * 100)) > 1;''')
# connect to news database and run Query
def get_title(Query):
    dbconnect = None
    try:
        dbconnect = psycopg2.connect ( database=DBName)
        c = dbconnect.cursor()
        c.execute(Query)
        row = c.fetchone()
        while row is not None:
            print " \n"+"* "+(str(row[0])),"---",(str (row[1])) 
            row = c.fetchone()
        c.close()
        return  ("  ")
    finally:
        if dbconnect is not None:
            dbconnect.close()
# print the result of Query 1&2
if __name__ == '__main__':
    print(request1 + " \n ") , get_title(Query1)
    print(request2 + "\n") , get_title(Query2) 
    print(request3 + "\n") , get_title(Query3) 
