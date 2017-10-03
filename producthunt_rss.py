# -*- coding: utf8 -*-
from xml.etree import cElementTree
import requests


def parse_producthunt_rss():
    # Getting top 10 items from Product Hunt
    prht_rss_feed = 'https://www.producthunt.com/feed?category=undefined'
    response = requests.get(prht_rss_feed)
    parsed_xml = cElementTree.fromstring(response.content)
    items = []
    for node in parsed_xml.iter():
        if node.tag == '{http://www.w3.org/2005/Atom}entry':
            item = {}
            for item_node in list(node):
                if item_node.tag == '{http://www.w3.org/2005/Atom}title':
                    item['title'] = item_node.text
                if item_node.tag == '{http://www.w3.org/2005/Atom}link':
                    item['link'] = item_node.text
            items.append(item)
    return items[:10]


