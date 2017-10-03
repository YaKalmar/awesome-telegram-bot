# -*- coding: utf8 -*-
import re
from xml.etree import cElementTree
import requests


def clean_tag_from_xmlns(node_tag):
    # Remove everything between curly braces
    clean_tag = re.sub(r'(\{.*?\})', '', node_tag)
    return clean_tag


def parse_producthunt_rss():
    # Getting top 10 items from Product Hunt
    prht_rss_feed = 'https://www.producthunt.com/feed?category=undefined'
    response = requests.get(prht_rss_feed)
    parsed_xml = cElementTree.fromstring(response.content)
    items = []
    for node in parsed_xml.iter():
        if clean_tag_from_xmlns(node.tag) == 'entry':
            item = {}
            for item_node in list(node):
                if clean_tag_from_xmlns(item_node.tag) == 'title':
                    item['title'] = item_node.text
                if clean_tag_from_xmlns(item_node.tag) == 'link':
                    item['link'] = item_node.text
            items.append(item)
    return items[:10]