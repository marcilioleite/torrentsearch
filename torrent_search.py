'''
Torrent Search. 

@author: Marcilio
'''
import requests

api_url = 'http://fenopy.se/module/search/api.php'
 
'''
Search torrents through Fenopy's API.

@return: Remote Torrent URI from the first search result.
'''
def first(keyword):
    url = '%s?keyword=%s&format=json' % (api_url, keyword)
    r = requests.get(url)
    return r.json()[0]['torrent']