query_category = '''
LOAD CSV WITH HEADERS FROM
'file:///Category.csv'
AS line FIELDTERMINATOR ','
MERGE (category:Category {categoryID: line.title})
  ON CREATE SET category.title = line.title;
'''

query_articles = '''
LOAD CSV WITH HEADERS FROM
'file:///Articles.csv'
AS line FIELDTERMINATOR ','
MERGE (article:Article {articleID: line.title})
'''

query_reader = '''
LOAD CSV WITH HEADERS FROM
'file:///Reader.csv'
AS line FIELDTERMINATOR ','
MERGE (reader:Reader {readerID: line.name})
  ON CREATE SET reader.nickname = line.nickname,reader.email = line.email;
'''

articles = [query_category, query_articles, query_reader]
