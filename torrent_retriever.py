'''
Torrent Retriever.

@author: Marcilio
'''
import urllib

'''
Retrieves from online Torrent to temporary file.

@return: temporary file's path.
'''
def retrieve(remote):
    return urllib.urlretrieve(remote)[0]
