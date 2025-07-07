import os

from connect_database import Neo4jConnection
from dotenv import load_dotenv

from queries.upload_queries import queries_data_upload


load_dotenv()


def main():

    conn = Neo4jConnection(
        uri=os.getenv('URI'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
        )
    conn.query('CREATE OR REPLACE DATABASE graphDb')
    for query_string in queries_data_upload:
        conn.query(query_string, db=os.getenv('DB_NAME'))


if __name__ == '__main__':
    main()
