from html.parser import HTMLParser


class YtChannelParser(HTMLParser):
    def __init__(self, verbose=False):
        super().__init__()
        self.channel_id = None
        self.verbose = verbose

    def handle_starttag(self, tag, attrs):
        if tag == "link" and attrs[0] == ("rel", "canonical"):
            url = attrs[1][1]
            self.channel_id = url.split("/")[-1]
            if self.verbose:
                print("=" * 10)
                print("Handle starttag....")
                print("tag =", tag)
                print(attrs)
                print("=" * 10)
