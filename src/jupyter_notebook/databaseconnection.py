import os
from graphdatascience import GraphDataScience
from dotenv import load_dotenv

class DatabaseConnection:
    """ 
    This class is used to connect to the Neo4j database.

    Attributes:
        gds (GraphDataScience): The database connection.

    Methods:
        get_database_connection: Returns the database connection.
    """

    def __init__(self, endpoint:str="", username:str="", password:str="", database:str="neo4j"):
        """
        Initializes the DatabaseConnection class.

        Parameters:
            endpoint (str): The endpoint of the Neo4j database.
            username (str): The username of the Neo4j database.
            password (str): The password of the Neo4j database.
            database (str): The database of the Neo4j database.
        """

        load_dotenv()
        self.gds = GraphDataScience(
            endpoint or os.environ["NEO4J_ENDPOINT"], auth=(username or os.environ["NEO4J_USERNAME"], password or os.environ["NEO4J_PASSWORD"])
        )
        self.gds.set_database(database)

    def get_database_connection(self) -> GraphDataScience:
        """
        Returns the database connection.

        Returns:
            GraphDataScience: The database connection.
        """
        return self.gds
