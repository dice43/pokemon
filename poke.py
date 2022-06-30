import requests
import pandas as pd
import sqlalchemy as db
import random


def randPoke():
  pokeId = random.randrange(1,809,1)
  return pokeId

def toSearch():
  print("Do you wish to search the wild for Pokemon?")
  toExplore = input("Type 'Y' for yes or 'N' for no: ")
  if toExplore.upper() == 'N':
    quit()
    
def getPokemonInfo(data):
  id = data['id']
  name = data['name']
  types = ''
  count = 0
  for el in pokemonData['types']:
    count += 1
    if count > 1:
      types += ' and ' 
    types += str(el['type']['name'])

def getMoves(data):
  movelist = []
  movelist.append(data['moves'][0]['move']['name'])
  return movelist

def getTypes(data):
  types = []
  for type in data['types']:
    types.append(type['type']['name'])
  return types
  

#starter = input("Please enter the pokemon that you choose: ")
#url = 'https://pokeapi.co/api/v2/pokemon/' + starter.lower()

#Setting url to get pokemon from pokeAPI 
url = 'https://pokeapi.co/api/v2/pokemon/'

trainerParty = []

#Start of program ask if user wants a pokemon encounter
#toSearch()

#Start of the encounter by fetching a random pokemon id and catching the pokemon
pokeId = randPoke()

response = requests.get(url + str(pokeId))
pokemonInfo = response.json()

desiredInfo = ['id','name','moves','types']
moves = getMoves(pokemonInfo)
types = getTypes(pokemonInfo)
#print(moves)
print(types)
result = {
  "id" : pokemonInfo['id'],
  "name" : pokemonInfo['name'],
  "moves" : moves,
  "types" : types
}

print(result)
'''
df = pd.DataFrame(result)
print(df)

id = pokemonInfo['id']
name = pokemonInfo['name']
types = ''
count = 0
for el in pokemonInfo['types']:
  count += 1
  if count > 1:
    types += ' and ' 
  types += str(el['type']['name'])

print(id)
print(name)
print(types)

df = pd.DataFrame(pokemonInfo['results'])
print(df)
'''


'''
  #Trys to convert pokemon dictionary into json if it fails the pokemon selected was invalid
  try:
    pokemonData = response.json()

    validInput = True
  except:
    print("That is not a pokemon that exists in the Nine regions")
    print('')



print('The pokemon you chose is ' + pokemonData['name'])
count = 0
types = ''
for el in pokemonData['types']:
  count += 1
  if count > 1:
    types += ' and ' 
  types += str(el['type']['name'])
  

if count == 1:
  print(f'The pokemon\'s type is {types}')
else:
  print(f'The pokemon\'s types are {types}')




  
  
  pandas = pd.DataFrame.from_dict(normal)
  #SQL
  engine = db.create_engine('sqlite:///pokemon.db')
  pandas.to_sql('starters', con=engine, if_exists='replace', index=False)
  query_result = engine.execute("SELECT * FROM table;").fetchall()
  print(pd.DataFrame(query_result))
  '''


