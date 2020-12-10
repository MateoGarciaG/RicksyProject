

"""
TEST CASES DATABASE MODULE
"""

from src.database.db_conection import connection

def test_connection():
    
    assert isinstance(connection(), object) == True