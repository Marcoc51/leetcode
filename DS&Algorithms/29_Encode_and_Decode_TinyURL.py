class Codec:
    def __init__(self):
        self.url = {}
        self.start = 1
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.url[self.start] = longUrl
        index = str(self.start)
        self.start += 1
        return self.base + index
    
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        index = int(shortUrl[-1])
        return self.url[index]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
