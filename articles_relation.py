import os

from connect_database import Neo4jConnection
from dotenv import load_dotenv

from queries.articles_relation_queries import relations


load_dotenv()


def main():

    conn = Neo4jConnection(
        uri=os.getenv('URI'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
        )
    conn.query('CREATE OR REPLACE DATABASE graphDb')
    for query_string in relations:
        conn.query(query_string, db=os.getenv('ARTICLES_DB'))


if __name__ == '__main__':
    main()
