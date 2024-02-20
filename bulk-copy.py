# bulk-copy.py

import csv
from datetime import datetime
import psycopg2
import time

file_name = "data.csv"
table_name = "accounts"
table_columns=("user_id", "processed", "created_at", "updated_at")

def measure_copy(conn):
    with open(file_name, "r") as file:
        count = sum(1 for line in file)
    print(f"Total rows = {count}")

    with open(file_name, "r") as file:
        with conn.cursor() as cursor:
            start_time = time.time()
            cursor.copy_from(file, table_name, sep=',', null='', columns=table_columns)
            end_time = time.time()
    conn.commit()
    print(f"COPY command took = {end_time - start_time} seconds")
    

def main():
    conn = psycopg2.connect(
        host='127.0.0.1',
        port=54320,
        user='postgres',
        password='pzS5dRWDUc7bu8Kr',
        database='users'
    )

    measure_copy(conn)

    conn.close()

if __name__ == "__main__":
    main()