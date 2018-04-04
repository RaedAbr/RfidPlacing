###############################################################################
# NFC PLACING REST SERVER
# V1
# 04.04.2018
###############################################################################
import sqlite3
from flask import Flask, request, jsonify
rest = Flask(__name__)

###############################################################################
# SETTINGS
###############################################################################
HOST = '0.0.0.0'
SERVER_PORT = 5000
SQLITE_FILE = "NFC.db"
###############################################################################

###############################################################################
# DATABASE FUNCTIONS
###############################################################################

db = sqlite3.connect(SQLITE_FILE)
cursor = db.cursor()

def db_token_exist(token):
    query = 'SELECT * FROM authorizations WHERE token=?;'
    cursor.execute(query, (token,))
    token_check = cursor.fetchone()
    if token_check:
        return True
    else:
        return False

def db_object_get(id):
    query = 'SELECT * FROM objects WHERE id=?;'
    cursor.execute(query, (id,))
    object = cursor.fetchone()
    return object

def db_object_insert_update(id, name, location):
    query = 'INSERT OR REPLACE INTO objects VALUES (?, ?, ?);'
    cursor.execute(query, (id, name, location));
    db.commit()
    return

def db_object_delete(id):
    query = 'DELETE FROM objects WHERE id=?;'
    cursor.execute(query, (id,));
    db.commit()
    return

def db_get_all_objects():
    cursor.execute('SELECT * FROM objects;')
    objects = cursor.fetchall()
    return objects

###############################################################################
# OBJECTS FUNCTIONS
###############################################################################

# Check if the given authorization token is valid. Return True/False
def authorization_is_valid(token):
    return db_token_exist(token)

def object_get(id):
    # Get object from database
    object = db_object_get(id)

    # Return object
    if object is None:
        return '', 404 # 404 = Not Found
    else:
        return jsonify(
            id=object[0],
            name=object[1],
            location=object[2])

def object_insert_update(id, name, location):
    db_object_insert_update(id, name, location)
    return '', 200

def object_delete(id):
    db_object_delete(id)
    return '', 200

###############################################################################
# ROUTES
###############################################################################

@rest.route("/")
def index():
    return 'NFC PLACING REST SERVER'

@rest.route("/<object_id>", methods=['GET', 'POST', 'DELETE'])
def info(object_id):

    # First we check the authorization
    authorization_header = request.headers.get('Authorization')

    if not authorization_is_valid(authorization_header):
        return '', 401 # 401 = Unauthorized

    # Since there the authorization is valid

    # GET method
    if request.method == 'GET':
        return object_get(object_id)

    # POST method
    if request.method == 'POST':
        object_name = request.form['name']
        object_location = request.form['location']
        return object_insert_update(object_id, object_name, object_location)

    #DELETE method
    if request.method == 'DELETE':
        return object_delete(object_id)

    #UNKNOWN method
    return '',400

###############################################################################
# MAIN
###############################################################################
if __name__ == "__main__":
    rest.run(host=HOST, port=SERVER_PORT)

###############################################################################
# APIDOC
###############################################################################
"""
@api {get} /:id Get
@apiName GetObject
@apiGroup Object
@apiDescription Get an object

@apiParam {String} :id Object ID

@apiHeader {String} Authorization Authorization token

@apiSuccess {String} id Object ID
@apiSuccess {String} name Object name
@apiSuccess {String} location Object location

@apiSuccessExample Success Response
      HTTP/1.1 200 OK
      {
        "id": "356a192b7913b04c54574d18c28d46e6395428ab",
        "name": "Table",
        "location": "A406"
      }

@apiError {Unauthorized} 401 Authorization token is not valid
@apiErrorExample Unauthorized
    HTTP/1.1 401 Unauthorized

@apiError {NotFound} 404 Object not found
@apiErrorExample Not Found
    HTTP/1.1 404 Not Found

"""

"""
@api {POST} /:id Add/Edit
@apiName InsertUpdateObject
@apiGroup Object
@apiDescription Insert an object or update it if exist

@apiParam {String} :id Object ID
@apiParam {String} name Object name
@apiParam {String} location Object location

@apiHeader {String} Authorization Authorization token

@apiSuccessExample Success Response
      HTTP/1.1 200 OK

@apiError {BadRequest} 400 Name and/or location parameter missing
@apiErrorExample Bad Request
    HTTP/1.1 401 Bad Request

@apiError {Unauthorized} 401 Authorization token is not valid
@apiErrorExample Unauthorized
    HTTP/1.1 401 Unauthorized

"""

"""
@api {delete} /:id Delete
@apiName DeleteObject
@apiGroup Object
@apiDescription Delete an object

@apiParam {String} :id Object ID

@apiHeader {String} Authorization Authorization token

@apiSuccessExample Success Response
      HTTP/1.1 200 OK

@apiError {Unauthorized} 401 Authorization token is not valid
@apiErrorExample Unauthorized Response
    HTTP/1.1 401 Unauthorized
"""
