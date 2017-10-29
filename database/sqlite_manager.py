import logging
import sqlite3


class SQLiteManager(object):
    def __init__(self, database):
        logging.basicConfig(level='INFO')
        self.logger = logging.getLogger(__name__)
        self.database = database

    def execute_command(self, query, args=None):
        """
        Executes a query against the local SQLite database

        :param query: The SQL statement to run
        :param args: Optional arguments to use in the statement
        :return: The result of the execution
        """

        with SQLiteWrapper(self.database) as sqlite_db:
            self.logger.debug('Executing: {0}'.format(query))

            if args:
                if isinstance(args, list):
                    sqlite_db.executemany(query, args)
                else:
                    sqlite_db.execute(query, args)
            else:
                sqlite_db.execute(query)

            if query.lower().startswith('select'):
                results = list(sqlite_db.fetchall())
            else:
                results = sqlite_db.lastrowid

        return results


class SQLiteWrapper(object):
    def __init__(self, database):
        self.database = database

    def __enter__(self):
        """ Open the database connection """
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Close the database connection """
        self.conn.commit()
        self.conn.close()
