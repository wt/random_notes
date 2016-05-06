#!/usr/bin/env python

from __future__ import print_function

import contextlib
import urllib2
import xml.etree.ElementTree

PINGDOM_PROBE_SERVERS_LIST_URL='https://www.pingdom.com/rss/probe_servers.xml'
PINGDOM_NS_URI='http://www.pingdom.com/ns/PingdomRSSNamespace'

def main():
    with contextlib.closing(
            urllib2.urlopen(PINGDOM_PROBE_SERVERS_LIST_URL)) as url:
        root = xml.etree.ElementTree.parse(url)

    for i in root.findall('channel/item/{{{}}}ip'.format(PINGDOM_NS_URI)):
        print('    acl is_from_pingdom src {}'.format(i.text.strip()))

if __name__ == '__main__':
    main()
