'''
Torrent Downloader.

@author: Marcilio
'''
import libtorrent
import util

'''
Download Class.

Represents a BitTorrent Download File.
'''
class Download:
    
    '''
    Init begins download.
    
    @param torrent: Torrent path.
    @param savepath: Path to save the downloaded file.
    '''
    def __init__(self, torrent, savepath):
        self.session = libtorrent.session()
        self.session.listen_on(6881, 6891)
        self.handle = self.session.add_torrent({
            'save_path': savepath,
            'ti': libtorrent.torrent_info(torrent)
        })
        print savepath
      
    '''
    @return: Filename
    '''
    def name(self):
        return self.handle.name()
        
    '''
    @return: True if download is ready. False otherwise.
    '''
    def ready(self):
        return self.handle.status().state == libtorrent.torrent_status.seeding
    
    '''
    @return: Percentage of download progress.
    '''
    def progress(self):
        return self.handle.status().progress * 100
    
    '''
    @return: Download rate in Kilobytes per second.
    '''
    def download_rate(self):
        return util.humanize_bytes(self.handle.status().download_rate)