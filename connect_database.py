from neo4j import GraphDatabase


class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        if self.driver is not None:
            self.driver.close()

    def query(self, query, db=None):
        assert self.driver is not None, 'Driver not initialized!'
        session = None
        response = None
        try:
            session = (
                self.driver.session(database=db)
                if db is not None else self.driver.session()
                )
            response = list(session.run(query))
        except Exception as e:
            print('Query failed:', e)
        finally:
            if session is not None:
                session.close()
        return response
