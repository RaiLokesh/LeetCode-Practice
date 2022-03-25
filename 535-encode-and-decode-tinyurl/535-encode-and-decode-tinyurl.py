class Codec:
    counter = 0
    dictionary = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        Codec.counter += 1
        Codec.dictionary['http://tinyurl.com/'+str(Codec.counter)] = longUrl
        return 'http://tinyurl.com/'+str(Codec.counter)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return Codec.dictionary[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))