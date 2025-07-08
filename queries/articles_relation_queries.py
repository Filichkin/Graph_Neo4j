query_category_articles = '''
LOAD CSV WITH HEADERS FROM
'file:///Category_articles.csv'
AS line
MATCH (category:Category {categoryID: line.title_category})
MATCH (article:Article {articleID: line.title_article})
CREATE (article)-[:IS_IN]->(category);
'''

query_read_articles = '''
LOAD CSV WITH HEADERS FROM
'file:///read_articles.csv'
AS line
MATCH (reader:Reader {readerID: line.name})
MATCH (article:Article {articleID: line.title_article})
CREATE (reader)-[:READ]->(article);
'''

relations = [query_category_articles, query_read_articles]
