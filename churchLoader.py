from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable


class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def create_constituent(self, church_name, conference_name):
        with self.driver.session(database="neo4j") as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.execute_write(
                self._create_and_return_constituent, church_name, conference_name)
            for row in result:
                print("Created constituency between: {ch}, {conf}".format(
                    ch=row['ch'], conf=row['conf']))

    @staticmethod
    def _create_and_return_constituent(tx, church_name, conference_name):
        # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
        # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
        query = (
            "CREATE (ch:Church { name: $church_name }) "
            "CREATE (conf:Conference { name: $conference_name }) "
            "CREATE (ch)-[:IS_MEMBER_OF]->(conf) "
            "RETURN p1, p2"
        )
        result = tx.run(query, church_name=church_name,
                        conference_name=conference_name)
        try:
            return [{"ch": row["ch"]["name"], "conf": row["conf"]["name"]}
                    for row in result]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

    def find_church(self, church_name):
        with self.driver.session(database="neo4j") as session:
            result = session.execute_read(
                self._find_and_return_church, church_name)
            for row in result:
                print("Found church: {row}".format(row=row))

    @staticmethod
    def _find_and_return_church(tx, church_name):
        query = (
            "MATCH (c:Church) "
            "WHERE c.name = $church_name "
            "RETURN c.name AS name"
        )
        result = tx.run(query, church_name=church_name)
        return [row["name"] for row in result]


if __name__ == "__main__":
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://34ee9985.databases.neo4j.io"
    user = "neo4j"
    password = "tGHNG2wFLE-Qti9pge6xKbpnoOKn7f-PphbDoT_QaQ4"
    app = App(uri, user, password)
    app.create_constituent("Alice", "David")
    app.find_church("Alice")
    app.close()
