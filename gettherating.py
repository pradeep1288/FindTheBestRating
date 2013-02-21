#!/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2

product_rating = dict()
rating  = []
def get_rating_from_amazon(url, product):
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content)

    product_summary_table = soup.find('table',id="productSummary")
    try:
        product_summary_table_entries = product_summary_table.find('tr').findAll('td')
        for i in range(1, 6):
            j = 3 * i
            rating.append(product_summary_table_entries[j].renderContents().replace('&nbsp;','').replace('(', '').replace(')',''))
        rating.reverse()
        product_rating[product] = rating
    except Exception, e:
        print e

url = "http://www.amazon.com/Apple-iPhone-16GB-White-Unlocked/product-reviews/B0097CZJEO/"
get_rating_from_amazon(url, "iphone")
print product_rating["iphone"]



