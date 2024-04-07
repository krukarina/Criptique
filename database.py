import psycopg2

hostname = "localhost"
database = "postgres"
username = "postgres"
password = "7E6giDiK7o"
port_id = 5432
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=password,
        port=port_id)

    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS criptiquedata (
    id INT PRIMARY KEY,
    socialmedianame VARCHAR(255),
    login VARCHAR(255),
    password VARCHAR(255)
    )
    """)
    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
