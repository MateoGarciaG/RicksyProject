
from src.database.db_conection import connection
import pytest

"""
TEST CASES DATABASE MODULE
"""

@pytest.mark.db_conection
def test_connection():
    
    assert isinstance(connection(), object) == True