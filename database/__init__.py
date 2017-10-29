import os

from .sqlite_manager import SQLiteManager
from .sqlite_statements import statements

sqlite_file = os.path.join(os.getcwd(), 'database', 'tournaments.sqlite')
sqlite_db = SQLiteManager(sqlite_file)

for statement in statements:
    sqlite_db.execute_command(statement)
