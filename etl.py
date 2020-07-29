import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    
      """
    This query is for loading data from S3 into staging tables on Redshift.
    
    Parameters:
          cur: PostgreSQL driver connection cursor
          conn: PostgreSQL driver connection pool

    Returns:
          None
    """
        
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    
      """
    This query is for processing the data in staging tables and loading into the analytics tables on Redshift
    
    Parameters:
          cur: PostgreSQL driver connection cursor
          conn: PostgreSQL driver connection pool 

    Returns:
          None
    """
        
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()