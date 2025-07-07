import os

from connect_database import Neo4jConnection
from dotenv import load_dotenv

from queries.relation_queries import (
    employee_order,
    order_product,
    product_category,
    supplier_product,
)


load_dotenv()


def main():

    conn = Neo4jConnection(
        uri=os.getenv('URI'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
        )
    conn.query('CREATE OR REPLACE DATABASE graphDb')
    conn.query(employee_order, db=os.getenv('DB_NAME'))
    conn.query(order_product, db=os.getenv('DB_NAME'))
    conn.query(supplier_product, db=os.getenv('DB_NAME'))
    conn.query(product_category, db=os.getenv('DB_NAME'))


if __name__ == '__main__':
    main()
