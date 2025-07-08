# NEO4J

### Пример реализации

<img src="neo4j.png" width="800" height: auto>

<img src="example_1.png" width="800" height: auto>

<img src="example_2.png" width="800" height: auto>

### Пример запроса

```
MATCH (reader:Reader)
MATCH (unread_article:Article)
WHERE NOT ((reader)-->(unread_article))
MATCH (article:Article)
WHERE ((reader)-->(article))
MATCH (unread_article)-[:IS_IN]->()<-[:IS_IN]-(article)
CREATE(rec: RecommendationArticleToReader {nickname: reader. nickname })
WITH rec, unread_article, reader
MERGE(rec)-[rel:USED_TO_PROMOTE {email: reader.email}]->(unread_article)
RETURN rec, unread_article, rel;
```