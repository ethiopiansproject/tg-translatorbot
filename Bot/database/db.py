from pymongo import MongoClient
from Bot.config import database_uri

client = MongoClient (database_uri)
db = client ["users"]["id"]

def save_user (id):
  if get_user (id)["exist"]:
    pass
  else:
    db.insert_one ({
      "id": id
    })

def get_user (id = None):

  res = db.find()
  rres = []
  for i in res:
      rres.append (i["id"])
  length = len (rres)
  is_exist = ""

  if not id:
    is_exist = id

  else:
    is_exist = str(id) in str (rres)

  return {
    "length": length,
    "exist": is_exist
  }

def get_all_users ():

  res = db.find()
  rres = []
  for i in res:
    rres.append ({"id": i["id"]})

  return rres
