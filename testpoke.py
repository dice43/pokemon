import unittest
import requests
from poke import getMoves, getTypes

class TestPoke(unittest.TestCase):

    def test_getMoves(self):
        pokemonInfo = self.getPokemon()
        moves = getMoves(pokemonInfo)
        self.assertEqual(len(moves),1)

    def test_getTypes(self):
        pokemonInfo = self.getPokemon()
        types = getTypes(pokemonInfo)
        self.assertGreaterEqual(len(types),1)
        self.assertLessEqual(len(types),2)

    def getPokemon(self):
        url = 'https://pokeapi.co/api/v2/pokemon/'
        pokeId = 1
        response = requests.get(url + str(pokeId))
        pokemonInfo = response.json()
        return pokemonInfo

if __name__ == '__main__':
    unittest.main()
    