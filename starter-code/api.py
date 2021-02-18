from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId # Permite localizar los Id de los registros de Mongo


client = MongoClient()
db = client.LabFlask 
collection = db.celebrities 


# Iteration 2: Listing Our Celebrities

# Creacion API 
app = Flask('LABFLASK')
@app.route('/')
def landing():
    return 'CelebritiesAPI'

# Celebrities id y nombre 
@app.route('/celebrities')
def all_celebrities():
    found = db.celebrities.find({},{'Name':1})
    return dumps(found)


# Iteration 3: The Celebrity Details
def  details(id):
    found = db.celebrities.find({'_id':ObjectId(id)},{'_id':0})
    return found

@app.route('/celebrities/details/<id>')
def celebrity_details(id):
    id =str(id)
    found = details(id)
    return dumps(found)

# Iteration 4: Adding New Celebrities
def add_new_celebrity (name, occupation,catch_phrase):
    dic = {
        'Name':f'{name}',
        'Occupation':f'{occupation}',
        'Catch phrase':f'{catch_phrase}',
        }
    new_celebrity = db.celebrities.insert(dic)
    return new_celebrity

@app.route('/celebrities/new/<name>/<occupation>/<catch_phrase>')
def new (name, occupation,catch_phrase):
    add_new_celebrity(name, occupation,catch_phrase)
    return

# Iteration 5: Deleting Celebrities
def deleting_celebrity (id):
    delete = db.celebrities.remove({'_id':ObjectId(id)})  
    return 
@app.route('/celebrities/delete/<id>')
def delete_celebrity (id):
    id = str(id)
    deleting_celebrity(id)
    return 
'''#Iteration 6: Editing Celebrities
def edit (id,name = None, occupation = None,catch_phrase = None):

    return celebrity_edited
@app.route('/celebrities/edit/<id>/<name>/<occupation>/<catch_phrase>')
def editing_celebrities (id):
    id = str(id)
    
    return 
'''

app.run(debug = True)