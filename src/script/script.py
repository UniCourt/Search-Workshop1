import psycopg2


def get_postgres_version():
    conn = psycopg2.connect(
        database="postgres", user='postgres', password='postgres', host='database',
        port='5432'
    )

    cursor = conn.cursor()

    cursor.execute("select version()")

    data = cursor.fetchone()
    conn.close()
    print(f'Postgres version: {data}')


if __name__ == "__main__":
    get_postgres_version()
