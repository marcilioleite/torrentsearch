'''
Torrent Retriever.

@author: Marcilio
'''
import urllib

'''
Retrieves from online Torrent to temporary file.

@return: temporary file's path.
'''
def retrieve(remote, name):
    return urllib.urlretrieve(remote, 'torrents/%s.torrent' % name)[0]
