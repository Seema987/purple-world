import psycopg2
import psycopg2.extras 
import os
DB_URL = os.environ.get("DATABASE_URL", "dbname=photo_db")

def sql(query,parameters=[]):
    connection = psycopg2.connect(DB_URL)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(query, parameters)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result