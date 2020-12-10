
"""
DATABASE MODULE
"""

import  pymongo


def connection(user='m001-student', password='m001-mongodb-basics'):
    
    try:
        
        MONGO_URL_ATLAS = f'mongodb+srv://{user}:{password}@sandbox.dec55.mongodb.net/?retryWrites=true&w=majority'
        mongo = pymongo.MongoClient(MONGO_URL_ATLAS, tlsAllowInvalidCertificates=False)
        
    except pymongo.errors.ConnectionFailure as conn_error:
        print("ERROR - Cannot connect to DataBase", conn_error)
    else:
        print('Correct Connection!!')
    
    return mongo

if __name__ == "__main__":
    pass