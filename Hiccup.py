import requests
# Set the target webpage
url = 'http://172.18.58.80/spicyx/'
r = requests.get(url)
# This will get the full page
print(r.text)

# This will get the status code
print("Status code:")
print("\t *", r.status_code)
# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
headers = {
    'User-Agent' : 'Mobile'
}
# Test it on an external site
url2 = 'http://172.18.58.80/headers.php'
rh = requests.get(url2, headers=headers)
print(rh.text)

import scrapy
class NEWSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.80/spicyx/']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {'Image Link': x.xpath(newsel).extract_first(),}

        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse)

import unittest

class Hiccup(unittest.TestCase):
    def test_program(self):
        print("Testing")

if __name__ == '__main__':
    unittest.main()



