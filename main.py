import os

from connect_database import Neo4jConnection
from dotenv import load_dotenv

from queries import queries_data_upload


load_dotenv()

query_string = '''
LOAD CSV WITH HEADERS FROM
'file:///Product.csv'
AS line FIELDTERMINATOR ','
MERGE (product:Product {productID: line.ProductID})
  ON CREATE SET product.productName = line.ProductName,
  product.UnitPrice = toFloat(line.UnitPrice);
'''


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
