import torrent_search
import torrent_retriever
import torrent_downloader
import time

online_torrent = torrent_search.first('suits s01e03')
local_torrent = torrent_retriever.retrieve(online_torrent)
download = torrent_downloader.Download(local_torrent, 'C:/Downloads')

while (not download.ready()):
    print '%d %% done' % (download.progress())
    print '%s' % (download.download_rate())
    time.sleep(1)