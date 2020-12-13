
import  pymongo

"""DATABASE MODULE: This module let to connect us to a mongoDB through MongoClient
"""

def connection(user='m001-student', password='m001-mongodb-basics'):
    """connection: This function connects mongoDB to get MongoClient

    Args:
        user (str, optional): It's user's value for URL ATLAS srv. Defaults to 'm001-student'.
        password (str, optional): It's password's value for URL ATLAS srv. Defaults to 'm001-mongodb-basics'.

    Returns:
        object: Returns a MongoClient object
    """
    
    try:
        
        MONGO_URL_ATLAS = f'mongodb+srv://{user}:{password}@sandbox.dec55.mongodb.net/?retryWrites=true&w=majority'
        mongo = pymongo.MongoClient(MONGO_URL_ATLAS, tlsAllowInvalidCertificates=False)
        
    except pymongo.errors.ConnectionFailure as conn_error:
        print("ERROR - Cannot connect to DataBase", conn_error)
    else:
        print('Correct Connection!!')
    
    return mongo

if __name__ == "__main__":
    print(connection.__doc__)