import json

path = "Bot/languages/en.json"

with open (path, "r") as file:
  data = json.load (file)

def reply (txt):

  if txt not in data:

    return "404 NOT FOUND"

  else:

    return data[txt]
