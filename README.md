#### The purpose of database creation for Sparkify.

The purpose of this database project is for Sparkify to move their data and processes to the cloud to accomodate the growth in their user base and song database. Their data is stored in an S3 bucket and comprised of a directory of JSON logs on user activity on the app as well another directory with JSON metadata on the songs in their app. 

The main goal of the project is to create a set of dimensional tables for data analytics and extraction of business insight by the analytics team. 
To create the dimensional tables the data in S3 would be extracted, staged in Redshift and transformed by running SQL statements that create the analytics tables from these staging tables. And to build an ETL pipeline for a database hosted on AWS Redshift.

### State and justify your database schema design and ETL pipeline.
Created a star schema using the song and event datasets. Schema has been optimized for the analytics team to run queries on the song play analysis.
The star schema is comprised of a fact table (songplays) and four-dimension tables (songs, artists, time and users). Also, an ETL pipeline written that to  load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift                                           
The decision to adopt the AWS redshift database cluster is a good one as it addresses the challenge of normalize the database by defining facts and dimension tables for a star schema was to reduce redundancy and increase the data integrity. Also, the normalization of the database will make the data more intuitive and easy to understand by the users thus they will be able to make simplified queries to retrieve the data insight they are looking for which solves the problem the analytics team in Sparkify are facing. 


Here is an explanation of the files used in the project:

Create_tables.py: this python file drops and creates the fact and dimension tables for the star schema in Redshift. File should be run always to reset the tables before each time the etl.py file is run.

dwh.cfg: contains redshift database cluster and IAM role information for connection to datawarehouse. 

Etl.py: This file is for loading data from S3 into staging tables on Redshift and then processing that data into the analytics tables on Redshift. 
 
Sql_queries: the file contains the SQL queries for creating the fact and dimension tables in the create_tables.py file as well as for inserting data into those tables and processing same from S3 using the etl.py file. The SQL statements will be imported into the create_tables.py and etl.py files respectively. 

Song data file: stored in S3 and consist of files in JSON format which are a subset of real data from the Million Song Dataset. Each file contains metadata about a song and the artist of that song and are partitioned by the first three letters of each song's track ID.

Log data file: stored in S3 and consist of activity log files in JSON format generated by an event simulator based on the songs in the song data file. The log files in the dataset are partitioned by year and month. 

Readme: this file introduces and explains other files in the project. It contains information that is commonly required to understand what the project is about.


How to run the Python scripts:
Step 1: Launch a redshift cluster and create an IAM role that has read access to S3..
Step 2: Add redshift database and IAM role info to dwh.cfg file. 
Step 3: Run create_tables.py to create the fact and dimension tables.
Step 4: Run etl.py file to load data from S3 to staging tables on Redshift and from staging tables to analytics tables on Redshift.
Step 5: Run some analytics queries on Redshift database to compare the results with the expected results.





