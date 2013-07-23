import torrent_search
import torrent_retriever
import torrent_downloader
import time

online_torrent = torrent_search.first('Suburgatory S02E04')
local_torrent = torrent_retriever.retrieve(online_torrent['torrent'], online_torrent['name'])
download = torrent_downloader.Download(local_torrent, 'C:/Downloads')

while (not download.ready()):
    print '%d%% pronto' % (download.progress())
    print '%sps' % (download.download_rate())
    time.sleep(1)