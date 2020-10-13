#
# I should probably use Auraxium for this stuff
#

import urllib.request
import json

from . import enums

# TODO: try to get this from file or environment variable, fall back to s:example as default.
# Learn which method is more secure for a server first. Same with bot token.
api_service_id = 's:example'

# There has to be a more sensible way of doing this, like by making
# api_url_params a class and making this the constructor.
def init_api_url_params():
    """ Set api_url_params to its default values """
    parameters = {
        'base': 'http://census.daybreakgames.com',
        'service_id': str(api_service_id),
        'verb': '',
        'namespace': 'ps2:v2',
        'collection': '',
        'identifier': '',
        'modifier': ''
        }
    return parameters

# A dictionary to hold parameters for the API's url.
api_url_params = init_api_url_params()


###############################################################################
# API Access
###############################################################################

# Subclass the default URL opener so we can provide our own User-Agent header.
class CustomURLopener(urllib.request.FancyURLopener):
    version = 'ps2buddy/0.1'

urllib._urlopener = CustomURLopener()


def generate_url(parameters):
    """Iterate through each item in api_url_params and make a URL from it"""
    url = ''

    for key, value in parameters.items():
        if value != '':
            url = url + value + '/'
        else:
            pass

    url = url[:-1] # Remove that filthy final slash
    return url

def get_char_data_by_name(username):
    """Get all the data about a character from the API and return it"""
    api_url_params = init_api_url_params() # TODO: remove when url params becomes a class
    api_url_params['verb'] = 'get'
    api_url_params['collection'] = 'character'
    api_url_params['modifier'] = '?name.first_lower=' + username.lower()
    api_url = generate_url(api_url_params)

    with urllib.request.urlopen(api_url) as response:
        char_data = response.read()
    return char_data


###############################################################################
# Parsing
###############################################################################

def parse_test(username):
    c_data = get_char_data_by_name(username.lower())
    x = json.loads(c_data)

    print(x['character_list'][0]['name'])
    print(x['character_list'][0]['name']['first'])

# Placeholder test code. Prints some basic data about the given character.
def parse_basic_char_data(char_data):
    x = json.loads(char_data)
    print('Name: \t \t' + x['character_list'][0]['name']['first'])
    print('Battle Rank: \t' + x['character_list'][0]['battle_rank']['value'])
    print('Faction: \t' + enums.Faction(int(x['character_list'][0]['faction_id'])).name)

def character_brief(char_data):
    pass
