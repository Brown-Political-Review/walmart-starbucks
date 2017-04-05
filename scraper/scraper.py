
import scraperwiki
import urlparse
import lxml.html
import urllib
import time

from lxml import html
import requests

storenumber = 1
tree = 1
# scraperwiki.sqlite.SCRAPERWIKI_DATABASE_NAME = WALMART_STORES
while storenumber < 100000:
    url = 'http://www.walmart.com/store/' + str(storenumber) + '/details/'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    if tree is not None:
        street = tree.xpath('//span[@itemprop="streetAddress"]/text()')
        locality = tree.xpath('//span[@itemprop="addressLocality"]/text()')
        region = tree.xpath('//span[@itemprop="addressRegion"]/text()')
        postcode = tree.xpath('//span[@itemprop="postalCode"]/text()')
        record = {}
        record['StoreID'] = str(storenumber)
        try:
            record['Street'] = street[0].strip()
        except:
            record['Street'] = ""
        try:
            record['Locality'] = locality[0].strip()
        except:
            record['Locality'] = ""
        try:
            record['Region'] = region[0].strip()
        except:
            record['Region'] = ""
        try:
            record['Postcode'] = postcode[0].strip()
        except:
            record['Postcode'] = ""
        print storenumber, record
        storenumber = storenumber + 1 
        scraperwiki.sqlite.save(["StoreID"], record)
