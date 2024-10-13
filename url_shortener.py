# url_shortener.py
import random
import string

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.base_url = "http://short.ly/"

    def shorten(self, original_url):
        # Generate a random short code
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_map[short_code] = original_url
        return self.base_url + short_code

    def expand(self, short_url):
        short_code = short_url.replace(self.base_url, "")
        return self.url_map.get(short_code, None)


url_shortener = URLShortener()
original_url = "http://google.com"
short_url = url_shortener.shorten(original_url)
print(f"Shortened URL: {short_url}")
print(f"Expanded URL: {url_shortener.expand(short_url)}")
