import urllib.request
import json

import enums

# TODO: try to get this from file or environment variable, fall back to s:example as default.
# Learn which method is more secure for a server first. Same with bot token.
api_service_id = 's:example'

api_url_dict = {
    'base': 'http://census.daybreakgames.com',
    'service_id': str(api_service_id),
    'verb': '',
    'namespace': 'ps2:v2',
    'collection': '',
    'identifier': '',
    'modifier': ''
    }


###############################################################################
# API Access
###############################################################################

# Subclass the default URL opener so we can provide our own User-Agent header.
class CustomURLopener(urllib.request.FancyURLopener):
    version = 'ps2buddy/0.1'

urllib._urlopener = CustomURLopener()


def generate_url():
    """Iterate through each item in api_url_dict and make a URL from it"""
    url = ''

    for key, value in api_url_dict.items():
        if value != '':
            url = url + value + '/'
        else:
            pass

    url = url[:-1] # Remove that filthy final slash
    return url

def get_char_data_by_name(username):
    """Get all the data about a character from the API and return it"""
    api_url_dict['verb'] = 'get'
    api_url_dict['collection'] = 'character'
    api_url_dict['modifier'] = '?name.first_lower=' + username.lower()
    api_url = generate_url()

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
