#!/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2
import json

product_rating_amazon = dict()
product_rating_cnet = dict()
rating  = []

url_amazon_iphone5 = "http://www.amazon.com/Apple-iPhone-16GB-White-Unlocked/product-reviews/B0097CZJEO/"
url_amazon_nexus4 = "http://www.amazon.com/Google-Nexus-Phone-16GB-Unlocked/product-reviews/B00ABPKHH0/"
url_cnet_iphone5 = "http://www.cnet.com/smartphones/apple-iphone-5/4852-6452_7-35022502.html"
url_cnet_nexus4 = "http://reviews.cnet.com/smartphones/lg-nexus-4/4852-6452_7-35517164.html"


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
        product_rating_amazon[product] = rating
    except Exception, e:
        print e


def get_rating_from_cnet(url, product):
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content)

    product_summary_table = soup.find('div', id='allRatings')
    try:
        rating = []
        product_summary_table_entries = product_summary_table.findAll('strong')
        for i in range(1,6):
            j = 2*i
            rating.append(product_summary_table_entries[j].renderContents());
        rating.reverse()
        product_rating_cnet[product] = rating
    except Exception, e:
        print e


get_rating_from_amazon(url_amazon_iphone5, "iphone5")
get_rating_from_amazon(url_amazon_nexus4, "nexus4")
get_rating_from_cnet(url_cnet_iphone5, "iphone5")
get_rating_from_cnet(url_cnet_nexus4, "nexus4")

print json.dumps(product_rating_cnet)
print json.dumps(product_rating_amazon)


