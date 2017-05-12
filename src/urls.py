
class url_manage(object):

    def __init__(self, start_url):
        self._url_queue = [start_url]
        self._visited_urls = []

    def get_url(self):
        url = self._url_queue.pop(0)
        return url

    def add_url(self, urls):
        for url in urls:
            if url not in self._visited_urls:
                self._url_queue.append(url)

    def url_done(self, url):
        self._visited_urls.append(url)

    def get_url_queue(self):
        return self._url_queue

