#!/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2
import json

product_rating = dict()
rating  = []
def get_rating_from_amazon(url, product):
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content)

    product_summary_table = soup.find('table',id="productSummary")
    try:
        rating = []
        product_summary_table_entries = product_summary_table.find('tr').findAll('td')
        for i in range(1, 6):
            j = 3 * i
            rating.append(product_summary_table_entries[j].renderContents().replace('&nbsp;','').replace('(', '').replace(')',''))
        rating.reverse()
        product_rating[product] = rating
    except Exception, e:
        print e

url_iphone = "http://www.amazon.com/Apple-iPhone-16GB-White-Unlocked/product-reviews/B0097CZJEO/"
url_nexus = "http://www.amazon.com/Google-Nexus-Phone-16GB-Unlocked/product-reviews/B00ABPKHH0/"
get_rating_from_amazon(url_iphone, "iphone")
get_rating_from_amazon(url_nexus, "nexus4")

print json.dumps(product_rating)


