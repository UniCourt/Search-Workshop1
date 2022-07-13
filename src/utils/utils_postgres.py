"""
Methods to set postgres connection and add data to database
"""
import sys
import psycopg2


def set_connection(logger):
    """
    Create and set the connection to the Postgres Database

    :param logger: Logger object
    :return:
    """
    # Change the below variables to connect to your local setup
    db_name = "db_name"
    user_name = 'workshop_user'
    password = 'workshop_user1'
    host_ip = '127.0.0.1'
    port = '5432'
    try:
        postgres_conn = psycopg2.connect(
            database=db_name, user=user_name, password=password,
            host=host_ip, port=port
        )

        return postgres_conn
    except Exception as exc:
        logger.error(f"Could not connect to Postgres Database: {exc}")
        sys.exit(1)


def load_data(data_frame, query, postgres_conn, logger):
    """
    Insert data into the Postgres Database

    :param data_frame: Pandas dataframe to be inserted
    :param query: Insert query
    :param postgres_conn: Postgres Database connection
    :param logger: Logger object
    :return:
    """

    data_list_of_tuple = [tuple(row) for row in data_frame.to_numpy()]
    cursor = postgres_conn.cursor()
    try:
        cursor.executemany(query, data_list_of_tuple)
        postgres_conn.commit()
        cursor.close()
    except psycopg2.DatabaseError as error:
        logger.error("Error: %s", error)
        postgres_conn.rollback()
        cursor.close()
