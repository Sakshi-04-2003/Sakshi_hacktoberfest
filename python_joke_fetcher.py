import requests

def get_joke():
  """fetches and prints a random joke"""
  url = "http://api.icndb.com/jokes/random"
  resp = requests.get(url)
  data = resp.json()
  print(data["value"]["joke"])

get_joke()
