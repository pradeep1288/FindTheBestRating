#!/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2

product_rating = dict()
def get_rating_from_amazon(url, product):
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content)

    product_summary_table = soup.find('table',id="productSummary")
    myregex = '<td align=\"right\" style=\"font-family\:Verdana\,Arial\,Helvetica,Sans-serif;;font-size:10px;\">\&nbsp\;(.*)</td>'
    try:
        product_summary_table_entries = product_summary_table.find('tr').findAll('td')
        for i in range(1, 6):
            j = 3 * i
            print product_summary_table_entries[j].renderContents().replace('&nbsp;','').replace('(', '').replace(')','')
    except Exception, e:
        print e

url = "http://www.amazon.com/Apple-iPhone-16GB-White-Unlocked/product-reviews/B0097CZJEO/"
get_rating_from_amazon(url, "iphone")



