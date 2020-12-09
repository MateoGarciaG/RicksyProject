
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

# def choose_collection(db, collection):
    
#     collection = db[f'{collection}']
    
#     return collection

# def insert_document(collection, document):

#     if len(document) == 1:
#         collection.insert_one(document[0])
#     else:
#         collection.insert_many(document)
    
# def update_document(collection, query, operation):
    
#     results = collection.update_many(query, operation)
    
#     return results


# def delete_document(collection, query={}):
    
#     if query != {}:
#         results = collection.delete_one(query)
    
#         return 'Se ha eliminado el documento'
    
#     else:
#         return 'No se ha ingresado ninguna query'
    
# def find_document(collection, query={}):
    
#     results = collection.find(query)
    
#     return results