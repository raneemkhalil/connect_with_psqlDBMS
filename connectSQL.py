import psycopg2
from config import config 

def get_queries(file_name='database.sql'):

    # read the sql file
    file = open(file_name, 'r')
    sql_file = file.read()
    file.close()
    # sort into an array
    queries = sql_file.split(';')
    queries.remove('')
    return queries


def connect():
    
    conn = None
    
    try:
        # read connection parameters
        kwargs = config()
        # connect to the PostgreSQL server 
        conn = psycopg2.connect(**kwargs)
        print('connected successfully')
        # create a cursor and connect to the current database
        cur = conn.cursor()
        # get the sql statement from the sql file
        queries = get_queries()
        
        for query in queries:
            # execute a statement(query)
            cur.execute(query)     
            print(query)

        # print the result of executed statement
        print(cur.fetchone())
        # close the curser
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
       
    finally:
        if conn is not None:
            # end the connection
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
    