from mediator.logic import IRequestComponentHandler
import requests as req

API_POKEMON = 'https://pokeapi.co/api/v2/'
API_UNIS = 'http://universities.hipolabs.com/search?country='


def call_api(url):
    response = req.get(url)

    if response.status_code == 404:
        return 'Not Found'
    if response.status_code != 200:
        print('here', response.status_code, url)
        raise Exception('API response: {}'.format(response.status_code))
    return response


class PokemonComponentHandler(IRequestComponentHandler):

    @staticmethod
    def handle(request):
        return call_api(f'{API_POKEMON}/pokemon/{request.pokemon}')


class UComponentHandler(IRequestComponentHandler):

    @staticmethod
    def handle(request):
        return call_api(f'{API_UNIS}{request.U}')
