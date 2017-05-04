
class url_manage(object):

    def __init__(self,start_url):
        self.url_queue = [start_url]
        self.visited_urls = []

    def get_url(self):
        url = self.url_queue.pop(0)
        return url

    def add_url(self,urls):
        for url in urls:
            if url not in self.visited_urls:
                self.url_queue.append(url)

    def url_done(self,url):
        self.visited_urls.append(url)

