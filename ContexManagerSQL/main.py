import psycopg2

conn = psycopg2.connect(
    database="test",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
)

conn.autocommit = True
cursor = conn.cursor()


sql3 = """select * from persons;"""
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)

sql2 = """COPY persons(first_name, last_name, dob, email)
FROM 'C:\\Users\\vaigole\\Documents\\Postgres\\persons_duplicates.csv'
DELIMITER ','
CSV HEADER;"""

cursor.execute(sql2)

sql3 = """select * from persons;"""
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)

conn.commit()
conn.close()
