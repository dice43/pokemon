import requests

validInput = False
while not validInput:
  starter = input("Please enter the pokemon that you choose: ")
  url = 'https://pokeapi.co/api/v2/pokemon/' + starter.lower()
  response = requests.get(url)

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

