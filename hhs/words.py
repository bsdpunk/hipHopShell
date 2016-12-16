import sys
import requests
import json
from pprint import pprint

#def bitstamp_price(api_key):
#    headers = {'content-type': 'application/json'}
#    endpoint = "https://www.bitstamp.net/api/v2/ticker/btcusd/"
#    r = requests.get(endpoint, headers=headers)
#    json_data = json.loads(r.text)

#    return(json_data)
def rhymes_with(api_key, one):
    headers = {'content-type': 'application/json'}
    endpoint = "https://api.datamuse.com/words?rel_rhy=" + one
    r = requests.get(endpoint, headers=headers)
    json_data = json.loads(r.text)

    return(json_data)




def sounds_like(api_key, one):
    headers = {'content-type': 'application/json'}
    endpoint = "https://api.datamuse.com/words?sl=" + one
    r = requests.get(endpoint, headers=headers)
    json_data = json.loads(r.text)

    return(json_data)


def related_to(api_key, one):
    headers = {'content-type': 'application/json'}
    endpoint = "https://api.datamuse.com/words?ml=" + one
    r = requests.get(endpoint, headers=headers)
    json_data = json.loads(r.text)

    return(json_data)


def rhymes_relate(api_key, one, two):
    headers = {'content-type': 'application/json'}
    endpoint = "https://api.datamuse.com/words?rel_rhy=" + one + "&ml=" + two
    r = requests.get(endpoint, headers=headers)
    json_data = json.loads(r.text)

    return(json_data)








